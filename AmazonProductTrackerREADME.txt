This program is used to identify which products are no longer sold by Amazon. The CSV file attached is for the method to run through the URLs and check them, and the batch is to automate the execution of the program. 

The program sends an email containing all the URLs that it suspects of being down to a list of recipients. You must have a gmail account to use this feature as it has to send it from your account.

Setup:
1. Download Python.
2. Using Pypi, use pip install to install bs4, pandas, email, selenium, and smtplib. (Some may already be installed)
3. In the CSV file, put your list of URLs that you want it to run through. It should only be one column with the column name of "URL"
4. At line 38, put the name of the CSV file that has the URLs. 
5. Now you will have to add the recipients and sender for the email part. At lines 48 and 54, input all the recipients you wish to include in the email burst.
6. At lines 53, 61, and 62 input the Gmail of the account you wish to send this burst from.
7. At line 62, input the password for the account you wish to send the email burst from.

The program is now ready for use

Setup of batch file to allow for easy execution:
1. In the first directory location, put the location of Python itself. This can be found by using the search bar and searching "Python" and then right clicking when it comes up and clicking "Open file location"
2. In the second directory, put the location of the Python program AmazonProductTracker.py



It will now run off the batch file. You can automate it using Task scheduler or any other scheduling program you have available. 


Created by Adam Nitecki(IVLIVSCAESAR44)