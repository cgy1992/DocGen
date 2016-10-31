
# DocGen - Documentation

DocGen is a custom python scripts to produce HTML documentation.

This documentation is based on tags you have to insert in your code.

It is recommended to use Sublime Text 2 with custom key map (Preferences-> Key Binding- User). I presonnaly use the ones below to comment my code more easily :
```JSON
    [{"keys": ["ctrl+shift+c"], "command": "insert_snippet", 
    "args": {"contents":"#@sep \n#@description \n#@last_check \n#@class_name \n#@input_type \n#@output_type"}},
    {"keys": ["ctrl+shift+n"],"command": "insert_snippet", 
    "args": {"contents":"#@end_page \n#@new_page"}}]
```     
Thus the shortcut "ctrl+shift+c" allows me to insert the tags bloc to comment a new function

``` python
#@sep  Subsection or space if void
#@description  description of the function
#@last_check  last_check - to fill manually
#@class_name  If the function is a method
#@input_type  
#@output_type
def your_func(var1,var2):
	return result
``` 

 **This full bloc needs to be used each time you want to document a function, otherwise the function will be ignored. You have to put the bloc just above the function as shown in the example above**


The package generates documentation according to thoses tags. You can also generate different pages of documentation. You can use the markers '@new_page' and '@end_page' to delimit your pages.


Here are the tags you can use :

**Bloc to describe a new function**
``` python
#@sep  Subsection or space if void
#@description  description of the function
#@last_check  last_check - to fill manually
#@class_name  If the function is a method
#@input_type  
#@output_type  
``` 

**Add a subsection**
``` python
#@sep  Subsection 
``` 

**Start/end a page of documentation**
``` python
#@new_page
#@end_page
``` 

**End of the document**
``` python
#@enddoc  
``` 
If this tags is not provided then the documation will stop after a default limit of 1000 lines after the last tag detected

## Example


```python
import DocGen.gen_doc as gen
from DocGen.doc import *
```


```python
input_path='./Example/sample.py'
output_folder_path='./Example/Output'
```


```python
gen.gen_page(input_path,output_folder_path)
```

    Documenation generated and saved in ./Example/Output
    
