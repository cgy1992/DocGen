#########################################
#Legend for commenting text
#@sep (use to parse the code)
#@description (explicite description of what the function does)
#@last_check (date of last edition of the code)
#@class_name (if method of one object : precise the name of the parent object else don't fill it)
#@input_type 
#@output_type
#
#<ul>
#<li><p><strong>file_data.print_d(string_content) </strong> <em> Last edit : </em></p>
#<p>INPUT : String</p>
#<p>OUTPUT : String - return log for debugging and load it in a text log file</p>
#</li>
#</ul>
#<div class="highlight"><pre><span class="k">def</span> <span class="nf">print_d</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">content</span><span class="p">):</span>
#</pre></div>
#########################################


import re

class doc_function:
	def __init__(self,description='',last_check='',class_name='',function_name='',input_type='',output_type='',first_line_fun='',args=''):
		self.description=description
		self.last_check=last_check
		self.class_name=class_name
		self.function_name=function_name
		self.input_type=input_type
		self.output_type=output_type
		self.args=args
		self.complete=False

	def to_html(self):		
		string='''
<ul>
<li><p><strong>%s.%s%s</strong> <em> Last edit : %s </em></p>
<p>INPUT : %s</p>
<p>OUTPUT : %s </p>
<p>DESCRIPTION : %s </p>
</li>
</ul>
<p></p>
<div class="highlight"><pre><span class="k">def</span> <span class="nf">%s</span><span class="p">%s:</span></pre></div>
'''% (self.class_name,self.function_name,self.args.replace('self,',''),self.last_check,self.input_type,self.output_type,self.description,self.function_name,self.args)
		return string
	
	def parse_get_args(self,line):
		output=re.search( r'.*def (.*)(\(.*\))',line)
		if output==None:
			output=re.search( r'.*class (.*)(\(.*\))',line)
		self.first_line_fun=line
		self.args=output.group(2)
		self.function_name=output.group(1)
		pass
	
	def check_fill(self):
		if(len(self.description)!=0 and len(self.last_check)!=0 and len(self.function_name)!=0 and len(self.input_type)!=0 and len(self.output_type)!=0 and len(self.args)!=0):
			self.complete=True
		pass

