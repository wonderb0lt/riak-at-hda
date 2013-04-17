Feature: Parsing the Frankfurt Galileo file

	Scenario: Parsing flight number
		Given testfile "fam-FRA-BKK-res.txt"
		When parsing
		Then field "id" should be "00QKXC"

	Scenario: Parsing users:
		Given testfile "fam-FRA-BKK-res.txt"
		When parsing
		Then passengers should include BECKER/ANNAMS (0)
		And passengers should include BECKER/ARNOLDMR (0)
		And passengers should include BECKER/ALEXANDERCHD (1)
		And passengers should include BECKER/ANNABELLEINF (2)

	Scenario: Parse flight header
		Given testfile "fam-FRA-BKK-res.txt"
		When parsing
		Then flight 0 has field "id" with value "TG921"
		And flight 0 has field "vendor_locator" with value "00V2NL"

	Scenario: Parse arrival/departure times
		Given testfile "fam-FRA-BKK-res.txt"
		When parsing
		Then flight 0 has int-field "departure" with value "1373467500" 
		And flight 0 has int-field "arrival" with value "1373523900"
		And flight 0 has int-field "duration" with value "38400"


	Scenario: Parse departure airport
		Given testfile "fam-FRA-BKK-res.txt"
		When parsing
		Then departure of flight 0 has field "Airport" with value "Frankfurt Intl"
		And departure of flight 0 has field "Terminal" with value "Terminal 1"
		And departure of flight 0 has field "IATA" with value "FRA"
		And departure of flight 0 has field "Location" with value "Frankfurt, Germany"


	Scenario: Parse arrival airport
		Given testfile "fam-FRA-BKK-res.txt"
		When parsing
		Then departure of flight 0 has field "Airport" with value "Suvarnabhumi Intl Arpt"
		And departure of flight 0 has field "IATA" with value "BKK"
		And departure of flight 0 has field "Location" with value "Bangkok, Thailand"

	Scenario: Parse other stuff
		Given testfile "fam-FRA-BKK-res.txt"
		When parsing
		Then flight 0 has field "Class" with value "Q"
		And flight 0 has field "Aircraft" with value "Airbus Industrie A380"
		And flight 0 has field "Services" which includes "Infant"
		But flight 0 has 0 stops
