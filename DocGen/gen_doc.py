import DocGen.doc as doc
import os
			
def gen_doc(code,limit=10000):
    end=False
    documentation=''
    i=0
    line=code.readline()
    while(i<limit and end==False):
        if('@sep' in line):
            documentation+= add_header(line,'@sep',header_level=2)[0]
            line=code.readline()
        if('@description' in line):
            nb_bloc_max=100
            n=0
            new_doc_function=doc.doc_function()
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
            #print(new_doc_function.to_html())
            documentation+=new_doc_function.to_html()+'\n'
        if('@end_page' in line):
            return(documentation,code)  
                
        line=code.readline()
        i+=1
    return(documentation,code)

def gen_page(input_path,output_folder_path,limit=1000):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    code=open(input_path,'r')
    end=False
    l=0
    while(end==False and l<limit):
        line=code.readline()
        if('@new_page' in line):
            page_title= add_header(line,'@new_page',header_level=2)[1]
            doc_page,code=gen_doc(code)
            page_path=output_folder_path+'/'+page_title+'.html'
            page=open(page_path,'w')
            page.write(doc_page)
        if('@enddoc' in line):
            end=True
        l+=1
    print('Documenation generated and saved in', output_folder_path)
    pass

def add_header(line,tag,header_level=2):
    output_title=line.replace(tag,'').replace('#','').replace(':','').strip()
    balise='''<h%s> %s </h%s> <a id='%s'></a>''' % (header_level,output_title,header_level,output_title)
    return balise,output_title



