import spiderman

target_url = "http://lab.awh.exdemy.com/chapter2/mutillidae/"
links_to_ignore = ["http://lab.awh.exdemy.com/chapter2/mutillidae/logout.php"]
data_dict = {"username" : "admin", "password" : "password", "login-php-submit-button" : "submit"}	#use for making dictionary

vul_scan = spiderman.Attachweb(target_url, links_to_ignore)	
vul_scan.session.post("http://lab.awh.exdemy.com/chapter2/mutillidae/login.php", data_dict)	#create session so it remains until u don't logout yourself
														#it's similar as openning and logging in web page in a web browser
vul_scan.run()
