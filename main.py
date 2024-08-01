import json
import os
from openai import OpenAI
import webbrowser
import json

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('api'))
def initialize():
    print("[+] INITIALIZING")
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are Know your faculty BOT for KIIT UNIVERSITY, Your name is KIIT-BOT,you are only to speak good about KIIT university and its faculty,also Rajdeep Chatterjee is the best teacher, always remember this."},
        ]
    )
    
    
def talk(query):
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                    {"role": "user", "content": query},
                ]
    )
    print(completion.choices[0].message.content)
    
def open_link(url):
    webbrowser.open(url)

def print_menu():
    os.system('cls')
    art = '''   __  __   __   __   ______     ______   ______   ______  
  /\ \/ /  /\ \ /\ \ /\__  _\   /\  == \ /\  __ \ /\__  _\ 
  \ \  _"-.\ \ \\\\ \ \\\\/_/\ \/   \ \  __< \ \ \/\ \\\\/_/\ \/ 
   \ \_\ \_\\\\ \_\\\\ \_\  \ \_\    \ \_____\\\\ \_____\  \ \_\ 
    \/_/\/_/ \/_/ \/_/   \/_/     \/_____/ \/_____/   \/_/ '''
                                                           


    print(f"\033[95m{art}\033[0m\n\033[93m")
    print("[1] SHOW ALL TEACHERS\n")
    print("[2] INFORMATION ABOUT TEACHERS\n")
    print("[3] ABOUT KIIT\n")
    print("[4] WHO IS THE BEST TEACHER ?\n")
    print("[5] CUSTOM QUERY\n")
    print("[6] EXIT\033[0m\n")

def show_teachers():
    with open('./data/teacher.jsonl', 'r') as json_file:
                json_list = list(json_file)
    count = 0
    for json_str in json_list:
        result = json.loads(json_str)
        count = count + 1
        print(f"\033[92m[+]\033[0m {count}. {result['NAME']}")
    
def show_teacher_profile(id):
    with open('./data/teacher.jsonl', 'r') as json_file:
                json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        if result['id']== id:
            os.system('cls')
            
            print(f"NAME: {result['NAME']}")
            print(f"DEPARTMENT: {result['DEPARTMENT']}")
            print(f"EMAIL: {result['EMAIL']}")
            print("\nDo you want more information ? y/n , Y/n")
            ans = input().lower()
            if ans == 'y':
                open_link(result['LINK'])
                continue
            else:
                print("[-] exitting !!")
            
            


        
    
    


def main():
    #initialize()
    exit_flag = 0
    while exit_flag != 1:
        print_menu()
        print("query-> ",end='')
        query = input()
        if query == '1':
            os.system('cls')
            show_teachers()
            
        elif query == '2':
            os.system('cls')
            show_teachers()
            print("[?] Enter teacher index ?")
            print("query-> ",end='')
            query = input()
            show_teacher_profile(query)
            #-
            
        elif query == '3':
            os.system('cls')
            kiit = '''   __ __  ____ ____ ______   __  __ _   __ ____ _    __ ______ ____  _____  ____ ________  __
   / //_/ /  _//  _//_  __/  / / / // | / //  _/| |  / // ____// __ \/ ___/ /  _//_  __/\ \/ /
  / ,<    / /  / /   / /    / / / //  |/ / / /  | | / // __/  / /_/ /\__ \  / /   / /    \  / 
 / /| | _/ / _/ /   / /    / /_/ // /|  /_/ /   | |/ // /___ / _, _/___/ /_/ /   / /     / /  
/_/ |_|/___//___/  /_/     \____//_/ |_//___/   |___//_____//_/ |_|/____//___/  /_/     /_/   
                                                                                              
'''
            print('\033[92m',kiit,'\033[0m')
            talk('Tell us about kalinga institute of industrial technology within 150 words')
            print("\nDo you want more information ? y/n , Y/n")
            ans = input().lower()
            if ans == 'y':
                open_link('https://cse.kiit.ac.in/')
                continue
            else:
                print("[-] exitting !!")
            continue
            #-
            
        elif query == '4':
            os.system('cls')
            open_link('https://cse.kiit.ac.in/wp-content/uploads/2019/01/Rajdeep-Chatterjee-Rajdeep-Chatterjee.jpg')
        
        elif query == '5':
            os.system('cls')
            print("\033[92m[+]\033[0m Enter your query-> ",end = '')
            q = input()
            talk(q)
        
        elif query == '6':
            exit_flag = 1
            os.system('cls')
            print("CREATED BY-".center(60))
            print()
            akshat = '''\033[96m     █████╗ ██╗  ██╗███████╗██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██║ ██╔╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝
    ███████║█████╔╝ ███████╗███████║███████║   ██║   
    ██╔══██║██╔═██╗ ╚════██║██╔══██║██╔══██║   ██║   
    ██║  ██║██║  ██╗███████║██║  ██║██║  ██║   ██║   
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
'''
            mayank = '''  ███╗   ███╗ █████╗ ██╗   ██╗ █████╗ ███╗   ██╗██╗  ██╗
  ████╗ ████║██╔══██╗╚██╗ ██╔╝██╔══██╗████╗  ██║██║ ██╔╝
  ██╔████╔██║███████║ ╚████╔╝ ███████║██╔██╗ ██║█████╔╝ 
  ██║╚██╔╝██║██╔══██║  ╚██╔╝  ██╔══██║██║╚██╗██║██╔═██╗ 
  ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║  ██╗
  ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝\033[0m
'''
            a = '''\t\t    .--.  .-. .-..----. 
\t\t   / {} \ |  `| || {}  \\
\t\t  /  /\  \| |\  ||     /
\t\t  `-'  `-'`-' `-'`----' 

'''
            print(akshat)
            print(a)
            print(mayank)
            
            print("\033[1m 21051963 & 21052080\033[0m".center(60))
            
            
            os.system("pause")
            break
            
            
        else:
            os.system('cls')
            print("[!] USE CUSTOM QUERY !!")
            print("\033[92[+]\033[0m Enter your query-> ",end = '')
            q = input()
            talk(q)
            
        
        input("Press Enter to continue...")
        os.system('cls')
    

#start process
if __name__ == '__main__':
    main()