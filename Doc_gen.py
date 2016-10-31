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
<p>OUTPUT : %s - %s </p>
<p></p>
</li>
</ul>
<div class="highlight"><pre><span class="k">def</span> <span class="nf">%s</span><span class="p">%s:</span></pre></div>
'''% (self.class_name,self.function_name,self.args.replace('self,',''),self.last_check,self.input_type,self.output_type,self.description,self.function_name,self.args)
        
        return string
    
    def parse_get_args(self,line):
        output=re.search( r'.*def (.*)(\(.*\))',line)
        self.first_line_fun=line
        self.args=output.group(2)
        self.function_name=output.group(1)
        pass
    
    def check_fill(self):
        if(len(self.description)!=0 and len(self.last_check)!=0 and len(self.function_name)!=0 and len(self.input_type)!=0 and len(self.output_type)!=0 and len(self.args)!=0):
            self.complete=True
            pass
			
			
			
def gen_doc(input_path):
    end=False
    documentation=''
    code=open(input_path,'r')  
    i=0
    line=code.readline()
    while(i<10000 and end==False):
 
        if('@end' in line or 'new_group' in line):
            end=True
        if('@sep' in line):
            documentation.write('''\* ===================================*\ \n''' ) 
            line=code.readline()
        if('@description' in line):
            nb_bloc_max=100
            n=0
            new_doc_function=doc_function()
            new_doc_function.description=line.replace('@description','').replace('#','').replace(':','')
            while(n<nb_bloc_max and new_doc_function.complete==False):
                line=code.readline()
                if('@description' in line):
                    new_doc_function.complete=True
                if('@last_check' in line):
                    new_doc_function.last_check=line.replace('@last_check','').replace('#','').replace(':','').replace(' ','')
                if('@input_type' in line):
                    new_doc_function.input_line=line.replace('@input_type','').replace('#','').replace(':','')
                if('@output_type' in line):
                    new_doc_function.output_type=line.replace('@output_type','').replace('#','').replace(':','')
                if('@class_name' in line):
                    new_doc_function.class_name=line.replace('@class_name','').replace('#','').replace(':','')            
                if('def ' in line):
                    new_doc_function.parse_get_args(line)
                    new_doc_function.complete=True
                n+=1               
            print(new_doc_function.to_html())
            documentation+=new_doc_function.to_html()+'\n'
        line=code.readline()
        i+=1
    return(documentation)
