function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"class\"/gi);
		if(m != null && m.length == 1){
			results.push(riakObject.key);
		}
	return results;
	}