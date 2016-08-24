import sys

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""
    
    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out

stepping = False
breakpoints = {9: True, 14: True}

##def debug(command, my_arg, my_locals): old command
def debug(command, my_arg, my_locals, lineno):
    global stepping
    global breakpoints
    
    if command.find(' ') > 0:
        arg = command.split(' ')[1]  
    else:
        arg = None  
    if command.startswith('s'):
        stepping = True
        return True
    elif command.startswith('c'):
        stepping = False
        return True
    elif command.startswith('q'):
        sys.exit(0)
    elif command.startswith('p'): #supposed to print all variables, not sure if that means stepping and breakpoints
        print stepping              #'p' is also supposed to var print as var = value
        print breakpoints
    elif command.startswith('b'): #supposed to set a breakpoint at a line
                                  #what does this entail??? what line are we adding a breakpoint to, why would we add a breakpoint to our current line????
        breakpoints.add[lineno] = True
    elif command.startswith('w'): #supposed to allow a var to set a watchpoint
                                   #im not really sure what a watchpoint does in the first place.....
    else:
        print "No such command available.", repr(command)
   
#this is the command list.

commands = ['s','s','b','w','q'] 


def input_command():
    #command = raw_input(" (my-spyder) ")
    global commands
    return commands.pop[0]
    
def traceit(frame, event, arg):
    global stepping
    global breakpoints
    
    if event == 'Line':
        if stepping or breakpoints.has_key(frame.f_lineno):
            resume = False
            while not resume:
                print event, frame.f_lineno, frame.f_code.co_name, frame.f_locals
                command = input_command()
                ##ok so below this comment is the old command for calling the debug method
                #resume = debug(command, arg, frame.f_locals) ##maybe we should add line numbers here so we can get breakpoint
                resume  = debug(command, arg, frame.f_locals,frame.f_lineno) ##and watchpoint done in debug method.
                ##above this comment is the new command for calling the debug method
    return traceit
    
    
sys.settrace(traceit)

print remove_html_markup('xyz')

sys.settrace(None)
