# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint

def execute():
	dn_list = [
	('DND/0050010', 'SOD/48969', 787.5), 
	('DND/0051725', 'SOD/50780', 540), 
	('DND/0054652', 'SOD/54352', 1518.75), 
	('DND/0058043', 'SOD/58082', 2587.5), 
	('DND/0058150', 'SOD/57767', 1346.62), 
	('DND/0058399', 'SOD/58518', 590.62), 
	('DND/0058691', 'SOD/58961', 6412.5), 
	('DND/0058681', 'SOD/58937', 1389.37), 
	('DND/0058682', 'SOD/58939', 1710), 
	('DND/0058683', 'SOD/58940', 865.68), 
	('DND/0058684', 'SOD/58941', 2565), 
	('DND/0058685', 'SOD/58942', 3526.87), 
	('DND/0058686', 'SOD/58944', 427.5), 
	('DND/0058687', 'SOD/58945', 673.31), 
	('DND/0058688', 'SOD/58946', 673.31), 
	('DND/0058689', 'SOD/58947', 1603.12), 
	('DND/0058692', 'SOD/58958', 1389.37), 
	('DND/0058785', 'SOD/59012', 843.75), 
	('DND/0058960', 'SOD/58027', 338.62), 
	('DND/0058961', 'SOD/58028', 338.62), 
	('DND/0058962', 'SOD/58277', 29.52), 
	('DND/0058963', 'SOD/58278', 24.9), 
	('DND/0058964', 'SOD/58282', 92.25), 
	('DND/0059002', 'SOD/59058', 1265.62), 
	('DND/0059003', 'SOD/59059', 1670.62), 
	('DND/0059004', 'SOD/59060', 1569.37), 
	('DND/0059005', 'SOD/59061', 2075.62), 
	('DND/0059018', 'SOD/58665', 1670.62), 
	('DND/0059081', 'SOD/57237', 1771.87), 
	('DND/0059082', 'SOD/57238', 1366.87), 
	('DND/0059083', 'SOD/57239', 1040.62), 
	('DND/0059084', 'SOD/57240', 641.25), 
	('DND/0059085', 'SOD/57241', 450), 
	('DND/0059086', 'SOD/57244', 1192.5), 
	('DND/0059087', 'SOD/57245', 742.5), 
	('DND/0059088', 'SOD/57246', 517.5), 
	('DND/0059158', 'SOD/58680', 810), 
	('DND/0059179', 'SOD/59353', 495), 
	('DND/0059180', 'SOD/59354', 540), 
	('DND/0059182', 'SOD/58431', 450), 
	('DND/0059183', 'SOD/58432', 506.25), 
	('DND/0059206', 'SOD/59048', 978.75), 
	('DND/0059210', 'SOD/58572', 337.5), 
	('DND/0059211', 'SOD/58721', 421.87)
	]
	
	so_list = [
	('SOD/59355', 879.99), 
	('SOD/59356', 1199.99), 
	('SOD/59357', 1199.99), 
	('SOD/59358', 1699.99), 
	('SOD/59349', 393.75), 
	('SOD/59350', 365.62), 
	('SOD/59351', 365.62), 
	('SOD/59352', 365.62), 
	('SOD/59319', 17.21), 
	('SOD/59320', 25.31), 
	('SOD/59321', 63.78), 
	('SOD/59322', 101.25), 
	('SOD/59332', 1350), 
	('SOD/59328', 703.12), 
	('SOD/59198', 50.4), 
	('SOD/59199', 126), 
	('SOD/59200', 86.62), 
	('SOD/59201', 66.15), 
	('SOD/59202', 27.56), 
	('SOD/59240', 96.75), 
	('SOD/59241', 143.43), 
	('SOD/59242', 188.43), 
	('SOD/59243', 233.43), 
	('SOD/59244', 354.37), 
	('SOD/59245', 258.75), 
	('SOD/59246', 928.12), 
	('SOD/59247', 928.12), 
	('SOD/59249', 1361.25), 
	('SOD/59251', 450), 
	('SOD/59203', 0), 
	('SOD/59082', 410.06), 
	('SOD/59083', 531.56), 
	('SOD/59105', 1406.25), 
	('SOD/59106', 911.25), 
	('SOD/59107', 1181.25), 
	('SOD/59108', 1125), 
	('SOD/59150', 3150), 
	('SOD/59151', 1462.5), 
	('SOD/59152', 2700), 
	('SOD/59153', 2812.5), 
	('SOD/59154', 3150), 
	('SOD/59157', 76.95), 
	('SOD/59158', 94.5), 
	('SOD/59159', 175.5), 
	('SOD/59160', 141.75), 
	('SOD/59161', 270), 
	('SOD/59162', 91.12), 
	('SOD/59164', 1012.5), 
	('SOD/59165', 1215), 
	('SOD/59166', 1215), 
	('SOD/59167', 303.75), 
	('SOD/59168', 911.25), 
	('SOD/59169', 393.75), 
	('SOD/59063', 160.31), 
	('SOD/59080', 585.78), 
	('SOD/59081', 539.66), 
	('SOD/59111', 371.25), 
	('SOD/59112', 405), 
	('SOD/59113', 438.75), 
	('SOD/59114', 540), 
	('SOD/59115', 877.5), 
	('SOD/59116', 877.5), 
	('SOD/59117', 2025), 
	('SOD/59028', 78.75), 
	('SOD/59001', 839.99), 
	('SOD/59002', 799.87), 
	('SOD/59006', 337.5), 
	('SOD/59007', 641.25), 
	('SOD/59008', 708.75), 
	('SOD/59009', 213.75), 
	('SOD/59010', 900), 
	('SOD/59011', 303.75), 
	('SOD/59049', 1040.62), 
	('SOD/58880', 2250), 
	('SOD/58974', 2385), 
	('SOD/58975', 2160), 
	('SOD/58977', 101.47), 
	('SOD/58978', 101.25), 
	('SOD/58979', 101.25), 
	('SOD/58980', 73.12), 
	('SOD/58981', 73.12), 
	('SOD/58833', 2885.62), 
	('SOD/58882', 182), 
	('SOD/58951', 213.75), 
	('SOD/58949', 1763.43), 
	('SOD/58938', 1229.06), 
	('SOD/58943', 609.18), 
	('SOD/58724', 146.25), 
	('SOD/58744', 337.5), 
	('SOD/58725', 2081.25), 
	('SOD/58626', 1154.25), 
	('SOD/58495', 136.12), 
	('SOD/58497', 33.41), 
	('SOD/58498', 30.93), 
	('SOD/58499', 28.46), 
	('SOD/58500', 28.46), 
	('SOD/58502', 30.93), 
	('SOD/58503', 33.41), 
	('SOD/58504', 77.96), 
	('SOD/58539', 112.5), 
	('SOD/58540', 675), 
	('SOD/58541', 641.25), 
	('SOD/58542', 135), 
	('SOD/58543', 2250), 
	('SOD/58544', 1012.5), 
	('SOD/58545', 472.5), 
	('SOD/58546', 3825), 
	('SOD/58555', 76.95), 
	('SOD/58556', 159.3), 
	('SOD/58415', 2813.62), 
	('SOD/58419', 424.35), 
	('SOD/58421', 539.66), 
	('SOD/58422', 539.66), 
	('SOD/58423', 585.78), 
	('SOD/58323', 244.46), 
	('SOD/58111', 172.12), 
	('SOD/58114', 174.65), 
	('SOD/58116', 101.25), 
	('SOD/58143', 42.52), 
	('SOD/58181', 13500), 
	('SOD/58182', 10125), 
	('SOD/58123', 2244.37), 
	('SOD/58076', 922.5), 
	('SOD/58007', 39.6), 
	('SOD/58008', 55.68), 
	('SOD/58002', 673.31), 
	('SOD/56737', 38250), 
	('SOD/56738', 38250), 
	('SOD/57896', 11812.5), 
	('SOD/57768', 1350), 
	('SOD/57769', 3375), 
	('SOD/57770', 3375), 
	('SOD/57771', 1687.5), 
	('SOD/57772', 3375), 
	('SOD/57773', 675), 
	('SOD/57774', 675), 
	('SOD/57788', 20250), 
	('SOD/57789', 2025), 
	('SOD/57790', 2025), 
	('SOD/57791', 4050), 
	('SOD/57792', 4050), 
	('SOD/57793', 4050), 
	('SOD/57794', 4050), 
	('SOD/57736', 539.66), 
	('SOD/57712', 820.12), 
	('SOD/57288', 99.16), 
	('SOD/57290', 295.2), 
	('SOD/56050', 51.3), 
	('SOD/55558', 1181.25), 
	('SOD/55559', 1181.25), 
	('SOD/55206', 421.87), 
	('SOD/54968', 3976.87), 
	('SOD/54732', 189.84), 
	('SOD/52655', 135), 
	('SOD/51677', 27000), 
	('SOD/51609', 3375), 
	('SOD/51610', 3375), 
	('SOD/38657', 843.75), 
	('SOD/38327', 4725), 
	('SOD/32483', 540), 
	('SOD/23490', 4725), 
	('SOD/22752', 2362.5), 
	('SOD/22678', 2025), 
	('SOD/22679', 2025), 
	('SOD/22682', 3712.5), 
	('SOD/17524', 4050), 
	('SOD/17525', 4050), 
	('SOD/17526', 1012.5), 
	('SOD/11449', 1350), 
	('SOD/07192', 2362.5), 
	('SOD/07193', 2025), 
	('86837', 2025), 
	('53348', 21937.5), 
	('38750', 2700), 
	('SOD/02339', 2025), 
	('SOD/02340', 3375), 
	('SOD/02341', 4050), 
	('SOD/02342', 4050), 
	('SOD/02374', 2025), 
	('SOD/02375', 1687.5)
	]
	for i in range(len(dn_list)):
		frappe.db.sql("""UPDATE `tabDelivery Note Item`
			SET rate = %s, amount = rate * qty
			WHERE name = %s """, (dn_list[i][2], dn_list[i][0]))
		print ("Updated Prices in Delivery Note Detail# " + dn_list[i][0] + " to " + dn_list[i][2])
		frappe.db.sql("""UPDATE `tabSales Order Item`
			SET rate = %s, amount = rate * qty
			WHERE name = %s """, (dn_list[i][2], dn_list[i][1]))
		print ("Updated Prices in Sales Order Detail# " + dn_list[i][1] + " to " + dn_list[i][2])
	
	for i in range(len(so_list)):
		frappe.db.sql("""UPDATE `tabSales Order Item`
			SET rate = %s, amount = rate * qty
			WHERE name = %s """, (so_list[i][1], so_list[i][0]))
		print ("Updated Prices in Sales Order Detail# " + so_list[i][0] + " to " + so_list[i][1])