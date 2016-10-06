import xlrd
import xml.dom.minidom as Dom

data = xlrd.open_workbook('numbers.xls')
table = data.sheet_by_name(u'numbers')

L = []
for i in range(table.nrows):
	v = table.row_values(i)
	L.append(list([int(v[0]), int(v[1]), int(v[2])]))

class XMLGenerator:

	def __init__(self, xml_name):
		self.doc = Dom.Document()
		self.xml_name = xml_name

	def createComment(self, data):
		return self.doc.createComment(data)

	def createNode(self, node_name):
		return self.doc.createElement(node_name)

	def addNode(self, node, prev_node = None):
		cur_node = node
		if prev_node is not None:
			prev_node.appendChild(cur_node)
		else:
			self.doc.appendChild(cur_node)
		return cur_node

	def setNodeAttr(self, node, attr_name, value):
		cur_node = node
		cur_node.setAttribute(attr_name, value)

	def setNodeValue(self, cur_node, value):
		node_data = self.doc.createTextNode(value)
		cur_node.appendChild(node_data)

	def genXml(self):
		with open(self.xml_name, 'w') as f:
			f.write(self.doc.toprettyxml(indent='\t', newl='\n', encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
	# generate XMLGenerator instance
	myXMLGenerator = XMLGenerator('numbers.xml')
	# create root node
	node_root = myXMLGenerator.createNode('root')
	# add root node
	myXMLGenerator.addNode(node_root)
	# create numbers node
	node_numbers = myXMLGenerator.createNode('numbers')
	# add numbers node
	myXMLGenerator.addNode(node_numbers, node_root)
	# create comment
	node_comment = myXMLGenerator.createComment('\t数字信息')
	# add comment node
	myXMLGenerator.addNode(node_comment, node_numbers)
	# set node value for numbers
	myXMLGenerator.setNodeValue(node_numbers, '{\n\t%s,\n\t%s,\n\t%s\n}' % (L[0], L[1], L[2]))

	myXMLGenerator.genXml()
