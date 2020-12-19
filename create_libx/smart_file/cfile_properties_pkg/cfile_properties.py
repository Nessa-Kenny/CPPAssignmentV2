#library package - createf_example_pkg7
class CreateFile:

	def createf(self, title, ing, meth, notes, kw):
		tit = title + '.txt'
		fh = open (tit,  "w")
    
		fh.write('Ingredients: \n\n')
		fh.write(ing + '\n\n\n')
	    
		fh.write('Method: \n\n')
		fh.write(meth + '\n\n\n')
		fh.write('Notes: \n\n')	
		fh.write(notes + '\n\n\n')
		fh.write('Keywords: \n\n')
		fh.write(kw)
		fh.close()
		print("HERE")
    	#return upload_file(tit, BUCKET)

    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
