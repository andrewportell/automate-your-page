def generate_concept_HTML(concept_title, concept_description):
    html_text_1='''
<div class="concept">
    <div class="concept-title">
        '''+concept_title
    html_text_2='''
    </div>
    <div class="concept-description">
        '''+concept_description
    html_text_3='''
    </div>
</div>'''
    full_html_text =html_text_1 +html_text_2 +html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title=concept[0]
    concept_description =concept[1]
    return generate_concept_HTML(concept_title, concept_description)

MY_LIST_OF_CONCEPTS = [ 
['Functions', 'Functions are sometimes referred to as procedures. Functions are powerful because they allow text or integers to be input and an automatic output to be generated.   This is what we will use to generate our HTML when we automate out webpage.'],

['If and While', """If statements are used to control which code gets executed when conditions are met and While loops are used to perform repetitive tasks.
If example:
def biggest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
print biggest(9,5,3)
#>>>9

While loops:
while  <Test Expression>:
    <block>
i = 0
while i != 10:
    i = i + 1
    print i
This example will print 1-10 and then become false since 10 would be equal to 10 and != stands for not equal.   
Use Break to stop executing the existing loop and move on to the next code."""],

['Equality Comparisons', """Python has many operators available for making comparisons
< less than, > greater than, <= less than or equal to, etc.
<number> <operator> <number>
Boolean value: value True or value False
print 2 < 3
True 
print 21 < 3
False
print 7 * 3 < 21
False
print 7 * 3 != 21     #   != stands for not equal to
False
print 7 * 3 == 21     #   == stands for equal to
True"""], 

['The OR Operator', '<Expression> or <Expression> In cases where the first expression evaluates to True, the value is True and the second expression is not evaluated. If the first expression evaluates to False, the value is the value of the second expression.'],

['Break', """Break is used to exit a loop if the while statement is true, but if the break is true it will move on out of the current while loop to the next code."""],

['Debugging', """When debugging code examine the Python Tracebacks to see what went wrong.  Pay attention to the bottom half of the error message that indicates the line the error occurred and error description.   See the listed URL for a complete description of the error if needed.   
Another strategy is to add print statements within the code to evaluate the progress  and identify bugs midstream in the code."""],

['Median', """# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.
# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
def biggest(a,b,c):
    return bigger(a,bigger(b,c))
def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)
print(median(1,2,3))
#>>> 2
print(median(9,3,6))
#>>> 6
print(median(7,8,7))
#>>> 7"""],

['Writing Modular Code', 
"""Understand the Problem:  Develop an understanding of what the requirements for the project are and what the inputs and outputs will be.   Our problem in this stage is writing a Python program that will automatically generate (output) HTML when text (my notes) are input to the program.   
Make a Strategy:  Look at the existing HTML in the site focusing on how to structure the Python code to produce the content title and content description HTML. Then look at the text that will be the input. Structure the text with markers for the code to locate the Title and Description that will lead it to the content it will actually use in the website.   
Write Code in stages and keep refining it until the desired output is produced which will be usable HTML for use in our website."""]

]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML=""
    for concept in list_of_concepts:
        concept_HTML =make_HTML(concept)
        HTML =HTML +concept_HTML
    return HTML

print make_HTML_for_many_concepts(MY_LIST_OF_CONCEPTS)