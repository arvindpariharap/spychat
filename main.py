from default import spy_name ,spy_salataion ,spy_age ,spy_rating
Question =" Welcome to spychat /n are you a default user(Y/N)?"
choice =input(Question)
if choice =="Y" or "y":     #continue with default user infomation:
    start_chat(spy_name,spy_age ,spy_rating)
elif choice == "N" or "n":
    spy_name = input("tell me you name first:")
    if len(spy_name)>0:
          spy_salataion = input ("Welcome " + spy_name  + " what should i call you mr./miss?")
          spy_name = spy_salataion + "" + spy_name
          spy_age =input ("ok "+ spy_name + " enter your age ")
          spy_age =int(spy_age)
          if spy_age>12 and spy_age<60:
             spy_rating = input(" how much like it " + spy_name)
             spy_rating =float(spy_rating)
             if spy_rating>= 4.5:
                print("great! you are an ace user")
             elif spy_rating<4.5 and spy_rating>=3.5:
                print("good soon to be ace1!")
             elif spy_rating<3.5 and spy_rating>=2.5:
                print("you are doing good")
             else:
                print("try more, you can do better")
                is_online = true
                print("Welcome " + spy_name +" age: "+ str(spy_age) +" and ratting: "+ spy_ratting + " We are proud to have you onboard")
          else:
             print("oops! sorry,you are not of connect age to be our spy")
    else:
          print("sorry you have entered an invalid name!")
          def start_chat(spy_name,spy_age,spy_rating):
              current_status_msg = None
              show_menu = true                                  #adding a menu bar in chat function
              while show_menu == true:                        #status update statament
              print(" = = = = = = MENU = = = = = =\n")
              menu = """ what to do want to do?
              1. update a status.
              2. add a new friend.
              3. send a secreat message
              4. read a personal message.
              5. read chats from user."""
              menu_choice = input(menu)
              menu_choice = int(menu_choice)

              if menu_choice == 1:
                                 #input update status
              elif menu_choice == 2:
                                    #add friend module
              elif menu_choice == 3:
                                     #send a secreat message
              elif m enu_choice == 4:
                                    #read a message
              elif menu_choice == 1:
                                   # read a chat
              elif menu_choice == 0:
                  show_menu == False
              else:
                  print("oops! you have entered a wrong choice")
                                            # default message

             def add_status(current_status_msg):
                if current_status_msg! = None:
                     print("you current status is %s" %(current_status_msg))
                else:
                    print("you don't have any statusr right now")
                    default = input("do you want to select from your older status(Y/N)?")
                    if default.upper() == "N":
                        new_status_msg = input('whats on your mind?')
                        if len(new_status_msg)>0:
                            updated_status = new_status_msg
                        else:
                            ("you have note entered any status\n please to you again")
