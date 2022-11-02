#!/usr/bin/env python
import docx
import subprocess

doc = docx.Document('radni_plan.docx')

def translate_work_plan():
    text_out = open('work_plan.txt','w')
    for t in doc.tables:
        text_out.write("Table"*20+'\n')
        for r in t.rows:
            print('-'*50)
            text_out.write('-'*100+'\n')
            for c in r.cells:
                if c.text:
                    out = subprocess.check_output('trans -b "%s"' %c.text,shell=True)
                    c.text = out.decode()
                    print(c.text)
                    text_out.write(c.text)
    text_out.close()

if __name__ == "__main__":
    translate_work_plan()

