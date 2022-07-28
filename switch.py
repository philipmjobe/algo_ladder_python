# Sometimes it happens that we need to create an application with several pops up dialog boxes, i.e Page Frames. Here is a step by step process to create multiple Tkinter Page Frames and link them! This can be used as a boilerplate for more complex python GUI applications like creating interfaces for Virtual Laboratories for experiments, classrooms, etc.


# Here are the steps:

# Create three different pages. Here we have three different pages, The start page as the home page, page one, and page two.
# Create a container for each page frame.
# We have four classes. First is the tkinterApp class, where we have initialized the three frames and defined a function show_frame which is called every time the user clicks on a button.
# The StartPage is simple with two buttons to go to Page 1 and Page 2.
# Page 1 has two buttons, One for Page 2 and another to return to Start Page.
# Page 2 also has two buttons, one for Page 1 and others to return to StartPage.
# This is a simplistic application of navigating between Tkinter frames.
# This can be used as a boilerplate for more complex applications and several features can be added.

# The App starts with the StartPage as the first page, as shown in class tkinterApp. Here in StartApp, there are two buttons. Clicking on a button takes you to the respective Page. You can add images and graphs to these pages and add complex functionality. The pages have two buttons as well. Every time a button is pressed show_frame is called, which displays the respective Page.
