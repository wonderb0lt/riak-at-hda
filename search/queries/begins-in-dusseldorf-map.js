function(riakObject) {
	var count = 0;
	var m = JSON.parse(riakObject.values[0].data);
	if (m != null) {
		for (idx in m.flights) {
			if (m.flights[idx].from.iata == 'DUS') {
				count++;
			}
		}
	}
	return [count];
}