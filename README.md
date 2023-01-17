# Tour-and-Travel

Home Page






On running the web application, the screen that first displays is the home screen that displays a carousel showing the available offers of places to visit in Uganda and a tourist can be able to reserve.
On scrolling further down a list of the available destinations is displayed showing the available that are present in Uganda.
On clicking the view more, the user is taken to a page that shows them more about the destination that they want to go to, activities that are to be done in that destination and hotels that they can be able to sleep at depending on their choice.

At the bottom of the page that talks more about the destination that one has chosen, a book button is displayed at the bottom such that when the user clicks it, they are first made to login before they can further be taken to the payments page.




On the home page, when a user clicks the companies page they are displayed with a list of companies that are in charge of the tour and travels in Uganda to different destinations.



The company packages, mission and respective contact details are displayed. The user can be further taken to a page that displays all the activities and accomodation places provided by that company that has been selected.




When a company is selected, a list of the available packages is displayed and once the user clicks on any package they are taken to the activities and hotels that are available in that package.

Accommodation such as hotels available in the package that has been selected.




On clicking the Book now button, the user is taken to a login screen where they are required to first login before they can continue to the payment where their credit card details are to be filled.





After logging they are then taken to a page where they can be able to further make payments using paypal



After clicking the paypal button, the user is taken to a page where they fill in their respective details of how they are going to pay



A testimonial page appears where a list of previous customers who have enjoyed the service talk about how they liked the company and services offered.
On the Administrator side, they are required to first login with specified credentials before they can be able to access the system.





This is the dashboard that is displayed to the Administrator after they have logged in and this shows them a summary of the number of companies registered, packages available, registered customers and a list of the details for all the registered companies.





The Administrator can then also be displayed with a list of the customers who have been able to make payments.

The administrator is also displayed with a list of the packages available and for which company that they belong to.
DATABASE DESIGN / DATA STRUCTURE DESIGN
Tables and Relationship  In our Project Tour and travel, I used VISUAL STUDIO  as a front end and use SQL Lite 2008 as a backend.  Front end is mainly used for the designing purpose or designing the various kinds of forms and implement the logic and the backend is mainly used for, to store the data, records, or the information. We make all the tables in the SQL Lite 2008. 
My tables name are Add package, add package description, add source, add destination, add hotels, Hotel Rooms, Hotel Info, add adventures, delete and update adventure and city. These are the tables to store the records, data, and information in the back end means in the SQL Server 2008.
All the tables are used to store the records, and the administrator is able to watch all the data. Now we talk about the tables and how these tables work in a back end that we can know but the main thing is the relationship of the tables.  
That’s the most important thing for the back end. In my project there is a relationship between the tables which means all the tables are connected with each other so all the records or the data or the information can be easily stored and there is no chance of the mistakes in the tables.  
The Relationship between the tables is also considered as a security part if the records are not stored properly so the candidate is not able to work further so it can avoid the chance of the dummy records. 
Database
Add package: By this admin can add all details of packages. In this table PackageID is auto incremented and unique. Image will be uploaded by FileUpload control.
 
Add Destination: By this admin will add all Destination names and DestinationID will auto Incremented. DestinationID is the primary key.


Add accomodation: By this, an admin is able to add places of accommodation, the names of the hotel, location and an image of the hotel.

Add Testimonial: In this schema, a tourist is able to add their username, their profile image and a message describing how their tour has been, it’s a review that other tourists might want to check out. 
 



IMPLEMENTATION DETAILS
Admin Panel
Step 1: Register a company: In this step admin added package name and also uploaded image. When a company has been registered successfully it will show it registered successfully . Admin can add package, delete package, modify package and admin can also add all description of packages and add duration.

Step 2: Delete a company: By the following Edit button and Delete button Admin can update and delete details of a particular package. 
Step 3: Add Destination: Admin can add destination name. If Destination name is added in the database, it will show Saved in the label.
Step 4: Add Package Description: Admin added all the details of package and package name will select from Dropdown list which is referred from the database. 

Step 6: Add Hotel Details

Step 7: Add Transport Details
Step 8: Add Activity Details
User Panel: 
User Register: In this step new users must have to create an account. Login is possible only after the registration. Users can also change his/her password.

Step 2:  User Login: In this step registered customers can login/sign in the account. Login is possible only after the registration. Users can only login if they want to book a package and if they are registered 
Step 4: For booking, User will first login after login user can go to package panel this page will open. By this user can know details of package

Step 5: Booking Package: When the userWhen the user will click on the booking on the booking package button,  the user will go to the Payment.
Step 6: Payment: In this step the user will pay for the package.

Step 7: Viewing  services offered by the company

CONCLUSION
This web application provides an easy way to book tickets online. This application is designed in such a way that any further enhancements can be done with ease. Through this website users can book all packages of tourist places and hotels. By using this site we can save our time.




