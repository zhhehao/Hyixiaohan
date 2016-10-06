import xlrd
import xml.dom.minidom as Dom

data = xlrd.open_workbook('student.xls')
table = data.sheet_by_name(u'student')

d = {}
for i in range(table.nrows):
	v = table.row_values(i)
	v[2] = int(v[2])
	v[3] = int(v[3])
	v[4] = int(v[4])
	d[str(int(v[0]))] = v[1:]

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
	myXMLGenerator = XMLGenerator('student.xml')
	# create root node
	node_root = myXMLGenerator.createNode('root')
	# add root node
	myXMLGenerator.addNode(node_root)
	# create students node
	node_students = myXMLGenerator.createNode('students')
	# add students node
	myXMLGenerator.addNode(node_students, node_root)
	# create comment
	node_comment = myXMLGenerator.createComment('\t学生信息表\n\t"id" : [名字，数学，语文，英文]\n')
	# add comment node
	myXMLGenerator.addNode(node_comment, node_students)
	# set node value for students
	myXMLGenerator.setNodeValue(node_students, '{\n\t"1" : %s,\n\t"2" : %s,\n\t"3" : %s\n}' % (d['1'],d['2'],d['3']))

	myXMLGenerator.genXml()
