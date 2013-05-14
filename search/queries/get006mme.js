function(v) {
	var data = JSON.parse(v.values[0].data); 
	if(data.id == "006MME") {
		return [[v.key, data]]; 
	} 
	return []; 
}