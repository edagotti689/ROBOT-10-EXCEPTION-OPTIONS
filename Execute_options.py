# To know robot version
robot --version

# To get robot help
robot --help > robot_help.txt

# paasing values to variable through command line =>
    robot -v ONE:10 -v TWO:34 Loop.txt

# create log file for debug 
    robot -b debug.log test2_list.robot

# validate the test data
    robot --dryrun test2_list.robot

# To run particular test case and Test cases 
    robot -t "Add Two Values" first_test.txt
    robot -t Addition -t "Test Case 3" first_test.txt
    robot -t  Add* first_test.txt

# TO run a test case based on tag
    robot -i test2 first_test.txt

# TO run all test cases except given tag
    robot -e test2 first_test.txt

# Change logs path ==> 
    robot -d C:\Users\smellamp\Desktop\SRIRAM\INSTITUTION\COURSES\ROBOT_FRAMWEORK\Logs test2_list.robot

# To specifiy output.xml file name and skipe 
## -o or --output
    robot -o sriram.xml TEST_SUITE.robot
    # To skipe output.xml
    ''' NOTE :-- IF YOU SKIP OUTPUT.xml IT will SKIP log.html also'''
    robot -o NONE TEST_SUITE.robot

# To specifiy report.xml file name and skipe 
## -r or --report
    robot -r RRR.html TEST_SUITE.robot
    # To Skipe report.html
    robot -r NONE TEST_SUITE.robot

# To specifiy report.xml file name and skipe 
## -l or --log
    robot -l RRR.html TEST_SUITE.robot
    # To Skipe log.html
    robot -l NONE TEST_SUITE.robot
