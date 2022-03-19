# Photo Sharing Site
## About

As a keen amateur photographer I wanted a private site to share my photos.  Social Media offers a fine alternative, but, as an image owner, I was never happy with the lack of control I had over who says what about my images.  

This site was designed as a place for people to come together to share their own photos – whether they are professional or not.  The intention is to foster a community of photographers where ownership of content remains in their hands.

## UX

#### User Stories – Site User
* As a Site User I can view a list of images so I can choose which one to learn more about
* As a Site User I can search for images by tag so that I can only see images that I want to see.
* As a Site User I can click on an image to access more information it so that I can learn more about it.
* As a Site User I can upload my own images so that I can share my content.
* As a Site User I can delete my posts so that can retain control of my images
* As a Site User I can view comments made from other users so I can read an existing conversation and join in.
* As a Site User I can leave comments on a picture/post so that I can start/join a conversation
* As a site User I can like other users' pictures so that I can interact with the site
* As a Site User I can view the number of likes to see which image is more popular
* As a Site User I can Register for an account to be able to share my pictures.
* As I Site User I can reset my password so that I can log in if I forget my credentials.

#### User Stories – Site Admin
* As a Site Admin I can remove users so that I can ensure a code of conduct is followed
* As a Site Admin I can remove photos/posts so that I can keep the content family friendly
* As a Site Admin I can create draft content so that I can leave and finish it at a later time
* As a Site Admin I can upload photos/create posts so that I can manage my site's content.
* As a Site Admin I can remove comments that are offensive so I can keep the comment section family friendly
---

## Features
### Landing Page

![Home Page](pss-screenshots/home-page-not-logged-in.png)

The home page displays a thumbnail grid (Clocade View) of all of the published images on the site.  The navigation bar for users who are not logged in contains a 'login' and 'sign up' link.  The site title serves as a link to this page.

For logged in users:

![Home page](pss-screenshots/home-page-logged-in.png)

The thumbnail grid content remains the same, but the navigation bar now shows the users name, a link to the users page, a seach bar, a link to a page to upload an image and a log out link.
___ 
### User's Page:

The same grid has been employed for continuity purposes but this grid will display ONLY images that belong to the user - both published and draft.

![Users Page](pss-screenshots/users-page.png)
___

### Image Details

There are 3 image detail views: 
1 - for not logged in users
2 - public images for logged in users
3 - an image detail view for a user's own image

Image details for non-logged in users:

![Image Details](pss-screenshots/image-details-not-logged-in.png)

There is the picture in an enlarged form with information about it.  There is also the image's tags so a user can search for other images with the same tag.  There is NO option to 'like' this image nad no option to 'comment'

Image details for logged-in users:

![Image Details 2](pss-screenshots/image-details-logged-in.png)

There is now an option to 'like' the image with the ability to add a comment below:

![Comment Section](pss-screenshots/comments-section.png)
![Add a Comment](pss-screenshots/leave-a-comment.png)

Image details for User's own image:

![Image Details 3](pss-screenshots/image-details-draft.png)

This screensht shows an image which has not been made public yet.  There are instructions on how to do so.  Once it is made public, the user will see this:

![Image Details 4](pss-screenshots/image-details-published.png)
___

### Log In

The user is presented with a log in form that was styled using Crispy Forms.  Crispy Forms was chosen for all forms. There is also an option to reset passwords.

![Log In](pss-screenshots/log-in.png)
___ 

### Sign Up

The user must sign up with an email address as they will be unable to access the site without.  If the user fails to complete any field, the sign-up process will fail.

![Sign Up Screen](pss-screenshots/sign-up-screen.png)
___

### Forgot Password

The user will have an opportunity to reset their password by entering their email address and following a link that they will receive in their email.

![Reset Password](pss-screenshots/password-reset.png)
___

### Log Out

The user is not logged out on clicking the link in the nav bar, but directed to a confirmation page.

![Log Out](pss-screenshots/log-out.png)
___

### Upload an Image

This is the image upload screen where users can upload images in a number of formats, including but not limited to:'bmp', 'dib 'ps', 'flc', 'gif', 'png', 'ico', 'tiff', 'jpg', 'jpeg'.  It should be noted that RAW fils (.raw) cannot be uploaded.

![Upload an Image 1](pss-screenshots/upload-a-photo-pt1.png)
![Upload an Image 2](pss-screenshots/upload-a-photo-pt2.png)

___

### Edit an Image

If the user notices a spelling/factual error after publishing their image, they can fix it here.  They can also change the uploaded image.

![Edit Image](pss-screenshots/edit-photo.png)
___

### Delete an Image

The user will be given an opportunity to back out of the deletion process.  Once an image is deleted from the database it cannot be recovered.

![Delete Image](pss-screenshots/delete-image.png)

## Testing

### Manual Testing

There was no automated testing carried out during this project.  Each User Story was manually tested as follows:

* As a Site User I can view a list of images so I can choose which one to learn more about
    * On arrival at the website there is a grid of images clearly on display.  The User does not need to be logged in order to see this. A second grid of images, which includes the User’s (public/draft) images is available ONLY after registration/logging in
* As a Site User I can search for images by tag so that I can only see images that I want to see.
    * At the top of the screen is a search bar which the user can enter a term.  This will search the list of ‘tags’ that are put in by an image uploader.  If the search cannot find any tags, it returns a message stating that there were no results.  If it finds pictures with tags, it will display a search results page with all of the PUBLISHED images that contain the searched-for term. Draft images are excluded from the search.
* As a Site User I can click on an image to access more information it so that I can learn more about it.
    * Prior to logging in, from the landing page, the user can click on an image and read some limited information about the image.
    * After logging in, the user can click on an image and read more information about the image and also have the ability to read/add comments and likes.
    * After logging in, from the user’s personal page, the user can click on an image and read more information about it, including its status (published/draft).  
* As a Site User I can upload my own images so that I can share my content.
    * After logging in, a button will appear at the top of the screen saying ‘Upload Image’.  From here the user will be directed to a dedicated page where the user can upload an image with the following information: Title, Image, Description, Tags, Status.  The upload will not be successful if any of the fields are left blank.  This will display an error to the user.  
    * A successful upload will redirect the user to the user’s personal page where the new image will be located on the left.
    * There is also the option of leaving the page without saving a new image.  This will return the user to the user’s page.
* As a Site Admin I can create draft content so that I can leave and finish it at a later time
    * This was decided to be implemented for all users.  On the ‘Image Upload’ screen is an option regarding the status of an image – Published or Draft.  If the user chooses ‘Draft’, then the image will only be viewable from the User’s personal page, not the public feed.  If the user chooses ‘Published’ then image will be viewable from both. 
* As a Site User I can delete my posts so that can retain control of my images
    * When selecting an image from the user’s personal page, there is an option to delete the image that the user is currently looking at.  Selecting this option will direct the user to a ‘delete’ page which gives the user the opportunity to change their mind.  Once the image is deleted, it cannot be retrieved.
* As a Site User I can view/leave comments made from other users so I can read an existing conversation and join in.
    * After logging in, each picture that is selected will have a comments feature enabled.  From here, the user can read all of the exiting comments, or click a button that will take them a ‘Add Comment’ page.  This was chosen to be placed on a separate page for design purposes.
    * From this page, the user can write a comment in the empty field.  Clicking ‘Add Comment’ will direct he user back to the image.
* As a site User I can like/ view the number of likes other users' pictures so that I can interact with the site
    * After logging in, users will be able to click on an image and be presented an option to ‘like’ a picture.  Clicking on this button will change the image from a hollow heart, to a filled heart and also display text confirming that the user has liked the image.  A user can only like an image once.  This ‘like’ feature is not available from the user’s personal page, but the number of likes will be displayed.
* As a Site User I can Register for an account to be able to share my pictures.
    * On arrival at the site, in the top corner of the page is an option to ‘Sign Up’. This directs the user to a ‘Sign up’ page. On this page the user will be asked for a username, email address and a password (repeated).  The user cannot sign up if one or more fields are blank.
    * On completing this form, the user is directed to their email account to verify their email address.  The user cannot log in to the site without verifying their email.  
    * On clicking the link in the user’s email they will be directed to a page asking them to confirm their email address.  Clicking confirm will redirect them into the site and grants them access.
* As I Site User I can reset my password so that I can log in if I forget my credentials.
    * On the ‘Log In’ page there is an option ‘Forgot Password’.  Clicking this will take you to a page asking you to input your email address.  This sends an email to the address inputted.  Within this email is a link to a ‘change password’ page which will ask the user to enter a new password twice.  Should the passwords be valid, the user will see a screen confirming that their password has been changed.

* As a Site Admin I can remove users so that I can ensure a code of conduct is followed & 
* As a Site Admin I can remove photos/posts so that I can keep the content family friendly & 
* As a Site Admin I can remove comments that are offensive so I can keep the comment section family friendly
    * All of these are taken care of automatically by Django’s admin system.

### Bugs

|  Bug Number         | Problem                                                                                           | Cause                                                                                                                                                 | Solution                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Bug 1     | Registration form won't display in bootstrap styling                                              | Crispy Forms wasn't installed properly                                                                                                                | added 'crispy_forms' to installed apps                                                                                 |
| Bug 2     | Password Reset won't send email                                                                   | Django-Auth and Gitpod don't see eye-to-eye and will not send emails from a Google SMPT account.  This issue was not present when working in VS Code. | Removed django-auth and installed allauth.  The issue remained in Gitpod, but is not present in teh live site (Heroku) |
| Bug 3     | When adding new fields to Post model, migration failed repeatedly                                 | Unsure of underlying cause                                                                                                                            | Reset the database in Heroku                                                                                           |
| Bug 4     | Search Results not formatting correctly                                                           | Incorrect use of FOR loop                                                                                                                             | Rewrote FOR loop and placed it at the start of grid                                                                    |
| Bug 5     | Possible to upload 'blank' image                                                                  | Model was written to display a placeholder image without a placeholder being defined.                                                                 | Removed placeholder from model                                                                                         |
| Bug 6     | 'Like' button wasn't refreshing the page when user 'liked' a post                                 | Spelling mistake in django import.                                                                                                                    | Fixed the spelling mistake (HttpResponseRedirect)                                                                      |
| Bug 7     | 404 and 500 page outside of site                                                                  | No 404.html or 500.html page were created so django directed to the default                                                                           | Added a 404.html and 500.html page                                                                                     |
| Bug 8     | Users were able to access restrictted pages without logging in                                    | No privacy was associated with Upload/Edit/Delete image pages                                                                                         | Added LoginRequiredMixins to each class in views.py.                                                                   |
| Bug 9     | Comments were not displaying the comment author but were displaying the logged in user's username | The HTML was incorrect, user.username was defined and not comment.author                                                                              | Changed to comment.author                                                                                              |
| Bug 10    | Like button not symmetrical                                                                       | Padding added to bottom only                                                                                                                          | Added class mb-1 to icon                                                                                               |


Deployment
