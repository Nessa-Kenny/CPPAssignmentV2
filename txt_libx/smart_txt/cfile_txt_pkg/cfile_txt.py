#library package - createf_txt_example_pkg8
class CreateFileTxt:

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