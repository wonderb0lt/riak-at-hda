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