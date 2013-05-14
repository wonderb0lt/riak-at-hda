function(riakObject) {
		var results = [];
		var m = riakObject.values[0].data.match(/\"fares\"/gi);
		if(m == null){
			results.push(riakObject.key);
		}
	return results;
	}