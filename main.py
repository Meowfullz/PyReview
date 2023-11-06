from node.node import *

def main():
	pyreview()

def pyreview():
	head = node ("T", None)
	head = node ("K", head)
	head = node ("N", head)
	head = node ("I", head)
	head = node ("L", head)
	selection = head
	selection = selection.getLink()
	selection = selection.getLink()
	selection = selection.getLink()
	selection.addNodeAfter('E')
	selection = selection.getLink()
	selection.addNodeAfter('D')
	selection = selection.getLink()
	selection.addNodeAfter('L')
	selection = selection.getLink()
	selection.addNodeAfter('I')
	selection = selection.getLink()
	selection.addNodeAfter('S')
	print("The amount of Nodes head has is:", node.listlength(head))
	print('The amount of nodes selection has is', node.listlength(selection))

	#-------------------------------------------------------------------------------	tail = head
	
	tail = selection

if __name__ == "__main__":
	main()