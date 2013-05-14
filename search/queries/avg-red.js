function(v) {
	var total = 0.0;
	var sum = 0;
	for (i in v) {
		sum += v[i];
		total++;
	}
	var avg = sum/total;
	return [avg];
}