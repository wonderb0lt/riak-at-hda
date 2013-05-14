function(v) {
	var sum = 0
	var total = v.values.length;
	var data = JSON.parse(v.values[0].data);
	if (data.fares) {
		return [data.fares.taxes];
	} else {
		return []
	}

}