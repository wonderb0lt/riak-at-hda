http://docs.basho.com/riak/1.3.1/cookbooks/Riak-Search---Querying/
#search-cmd funktioniert weitestgehend mit dem format der lucene 2.9.1 api
#search / search-doc | id / document

#Die hier verwendeten MapReduce queries haben noch ein enormes optimierungspotential

#Den Buchungssatz mit der Buchungsnummer 009GH1
search-cmd search-doc FlightData id:009GH1
http://bdc-n-e4.fbi.h-da.de:8098/solr/FlightData/select?q=id:009GH1

#Den Buchungssatz mit der Ticketnummer 2203272401000
curl -XPOST http://bdc-n-e4.fbi.h-da.de:8098/mapred \
-H 'Content-Type: application/json' \
-d '{
	"inputs":"FlightData",
	"query":[{"map":{"language":"javascript",
	"source":"function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"eTicket\":\\s\"2203272401000/, \"i\");
		if(m != null){
			results.push(riakObject.key);
		}
	return results;
	}"}}]}'

#Alle Buchungen, die kein Direkt ug sind (d.h. mit Umsteigen)
curl -XPOST http://bdc-n-e4.fbi.h-da.de:8098/mapred \
-H 'Content-Type: application/json' \
-d '{
	"inputs":"FlightData",
	"query":[{"map":{"language":"javascript",
	"source":"function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"stops\":\\s\[\]/, \"i\");
		if(m != null){
			results.push(riakObject.key);
		}
	return results;
	}"}}]}'

#Alle Buchungen, die ein One-Way sind (d.h. ohne Rückflug)
curl -XPOST http://bdc-n-e4.fbi.h-da.de:8098/mapred \
-H 'Content-Type: application/json' \
-d '{
	"inputs":"FlightData",
	"query":[{"map":{"language":"javascript",
	"source":"function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"class\"/gi);
		if(m != null && m.length == 1){
			results.push(riakObject.key);
		}
	return results;
	}"}}]}'

#Alle Buchungen, die noch nicht ausgetellt wurden (d.h. kein Preis vorhanden)
search-cmd search-doc FlightData fares # Hier müsste man anzahl fares = 0 oder irgendwie auf nicht existenz prüfen TODO
curl -XPOST http://bdc-n-e4.fbi.h-da.de:8098/mapred \
-H 'Content-Type: application/json' \
-d '{
	"inputs":"FlightData",
	"query":[{"map":{"language":"javascript",
	"source":"function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"fares\"/gi);
		if(m == null){
			results.push(riakObject.key);
		}
	return results;
	}"}}]}'

#Alle Buchungen mit mehr als einem Passagier
curl -XPOST http://bdc-n-e4.fbi.h-da.de:8098/mapred \
-H 'Content-Type: application/json' \
-d '{
	"inputs":"FlightData",
	"query":[{"map":{"language":"javascript",
	"source":"function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"surname\"/gi);
		if(m != null && m.length > 1){
			results.push(riakObject.key);
		}
	return results;
	}"}}]}'

#Alle Buchungen, bei denen der Flug in Düsseldorf (DUS) begonnen wird
curl -XPOST http://bdc-n-e4.fbi.h-da.de:8098/mapred \
-H 'Content-Type: application/json' \
-d '{
	"inputs":"FlightData",
	"query":[{"map":{"language":"javascript",
	"source":"function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"iata\":\\s\"DUS\"/i);
		if(m != null){
			results.push(riakObject.key);
		}
	return results;
	}"}}]}'

#Die Anzahl der Buchungen, bei denen der Flug in Düsseldorf (DUS) begonnen wurde
curl -XPOST http://bdc-n-e4.fbi.h-da.de:8098/mapred \
-H 'Content-Type: application/json' \
-d '{
	"inputs":"FlightData",
	"query":[{"map":{"language":"javascript",
	"source":"function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"iata\":\\s\"DUS\"/i);
		if(m != null){
			results.push(1);
		}
	return results;
	}"}}, {"reduce":{"language":"javascript","source":"
	function(v) {
		var r = 0;
		for(var i in v) {
			r+=v[i];
		}
	return [r];
	}
"}}]}'

