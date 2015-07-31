## 4D Concepts Survey
##
## Writen by: Derek Naulls
## Author URI: http://www.4dconcepts.ca
## Facebook: /derek.naulls
## Twitter: @twinumbertwo
##

import sys

from datetime import datetime

class new_survey:

    def __init__(self):

        print('=======================================================================================') 
        print('                             4D Concepts Makerspace Survey')
        print('=======================================================================================\n')

        self.maker_space = raw_input(' Would you use a makerspace in Bancroft?: ')
        if self.maker_space.lower() != 'y' and self.maker_space.lower() != 'yes':
            print (' Okay. We\'ll try this again later.')

            # Opn a file for duds and record the time it was created
            self.f = open('duds.txt','a+')

            self.now = datetime.now()
            
            self.f.write('A dud survey was created at: ')
            self.f.write(self.now.strftime("%I:%M %p\n"))

            # Close the file once it is finished
            self.f.close()
           
            new_survey()
            
        self.uses = raw_input('\n What purpose would you use a makerspace for?: * Use a coma \',\' to separate types.\n\n (eg. research, protyping, social experiments, robotics, education...)\n\n ')

        self.equipment = raw_input('\n What type of equipment would you use?: * Use a coma \',\' to separate types.\n\n ')

        self.membership = raw_input('\n Would you pay for monthly membership?: ')
        if self.membership.lower() != 'n' and self.membership.lower() != 'no':
            self.membership_yes = raw_input('\n How much would you pay for a membership?: ')

        self.email = raw_input('\n Would you like to subscribe to updates regarding the Bancroft Makerspace?: ')
        if self.email.lower() != 'n' and self.email.lower() != 'no':
            self.email_yes = raw_input('\n What is your email?: ')

        self.comment = raw_input('\n Would you like to leave a comment?: ')
        if self.comment.lower() != 'n' and self.comment.lower() != 'no':
            self.comment_yes = raw_input('\n Type your comment here =>')

        print('\n Thankyou for taking the time to complete this survey! Your input if greatly')
        print(' valued and will be used to help develop an awsome makerspace where creative and')
        print(' inventive minds can come together and build amazing things.')

        # Opn a file for writing and create it if it doesn't exist
        self.f = open('surveyresults.txt', 'a+')

        self.f.write('\n-------------------- ')
        self.now = datetime.now()
        self.f.write(self.now.strftime("%I:%M %p "))
        self.f.write(' --------------------')
        self.f.write('\nWould you use a makerspace in Bancroft? {0}'.format(self.maker_space))
        self.f.write('\nWhat purpose would you use a makerspace for? {0}'.format(self.uses))
        self.f.write('\nWhat type of equipment would you use? {0}'.format(self.equipment))
        self.f.write('\nWould you pay for monthly membership? {0}'.format(self.membership))
        if self.membership.lower() != 'n' and self.membership.lower() != 'no':
            self.f.write('\nHow much would you pay for a membership? {0}'.format(self.membership_yes))
        self.f.write('\nWould you like to subscribe to updates regarding the Bancroft Makerspace? {0}'.format(self.email))
        if self.email.lower() != 'n' and self.email.lower() != 'no':
            self.f.write('\nWhat is your email? {0}'.format(self.email_yes))
        self.f.write('\nWould you like to leave a comment? {0}'.format(self.comment))
        if self.comment.lower() != 'n' and self.comment.lower() != 'no':
            self.f.write('\nComments:\n{0}'.format(self.comment_yes))

        # Close the file once it is finished
        self.f.close()

def main():

    x = 1
    while True:
        
        new_survey()

        f = open('surveyresults.txt', 'a+')
        f.write('\nSurvey number {0}'.format(x))
        f.write('\n---------------------------------------------------')

        f.close()
        
        x += 1
        
if __name__ == "__main__":
    main();
