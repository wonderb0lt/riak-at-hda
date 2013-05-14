function(v) {
	var data = JSON.parse(v.values[0].data);
	if (data && data.fares && data.fares.taxes) {
		return [data.fares.taxes];
	} else {
		return []
	}
}