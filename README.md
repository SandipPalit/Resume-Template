![Resume Template](/documentation/banner.jpg)

**I'm excited to introduce my latest creation: an online Resume Template powered by Python and Streamlit 📄**

This dynamic template offers a modern and professional look while allowing you to easily customize your resume with your own details and achievements. With interactive elements and a user-friendly interface, it's designed to make your resume not only informative but also engaging. Whether you're showcasing your skills to potential employers, clients, or connections, this template is the perfect tool to help you stand out in the digital landscape.

## Contents
* [**Setup the Code locally**](#setup-the-code-locally)
* [**Customize the Resume**](#customize-the-resume)
* [**Deploy on Streamlit Cloud**](#deploy-on-streamlit-cloud)
* [**Examples**](#examples)
* [**Reach out to Us**](#reach-out-to-us)

## Setup the Code locally

To transform this Resume Template, to your wonderful online Resume, we will follow some simple steps. Starting with getting a copy of the codebase, in our local machine.

To setup the code locally in our machine, we will follow these steps:
1. Fork this [Resume Template repository](https://github.com/SandipPalit/Resume-Template). ![Fork](/documentation/fork.jpg)
2. Download the Codebase on your Local machine.
3. Open the Codebase in PyCharm or any IDE of your choice.
4. Open Terminal and Run `pip install -r requirements.txt`, to install the necessary libraries.

> It will take some time, after which our setup will be completed.

## Customize the Resume

Now here comes the most interesting part, to customize this Resume Template we only need to change the content of some JSON files. Yes, you read it right!! We don't have to change any piece of code.

We can use Markdown text formatting in our text descriptions, like `**Bold**` for **Bold**, `_Italic_` for _Italic_, and `[Link](https://www.google.com)` for [Link](https://www.google.com).

Before customizing our code, we will start our streamlit app by running `streamlit run app.py` in the Terminal. The app will start on our default browser, and we will get the exact same UI as seen on [the Template](https://resume-template.streamlit.app/).

Now, all we need to do is, modify the files in the **assets** folder, which has the following file structure.

![Assets File Structure](/documentation/assets_file_structure.jpg)

###  _icon.png_

This is a generic icon image, as seen on the Tab. We can keep this image as it is.

###  _picture.jpg_

This is your Display Picture in the Header section. Replace this picture with your professional photo. Please note that your face should be clearly visible with proper lighting.

###  _resume.pdf_

This is your Resume that the users will be able to download from the Header section. Replace this file with your own Resume, in pdf format.

###  _01_sections.json_

This is the main Config file that Enables or Disables each of the sections. 

```json
{
  "SOCIAL_MEDIA" : true,
  "SKILLS" : true,
  "WORK_EXPERIENCE" : true,
  "EDUCATION" : true,
  "PROJECTS" : true,
  "PUBLICATIONS" : true,
  "PUBLIC_SPEAKING" : true,
  "CERTIFICATES" : true,
  "ACCOMPLISHMENTS" : true
}
```

By default, all the sections are enabled. To disable any section, navigate to `/assets/01_sections.json` file and change it's boolean value to `false`.

###  _02_header.json_

This section contains the Page Title and some basic information about you, like your Name and Description.

```json
{
  "PAGE_TITLE" : "",
  "NAME" : "",
  "DESCRIPTION" : ""
}
```

To customize this section, navigate to `/assets/02_header.json` file and update the following values:
* **PAGE_TITLE** : Enter the Title of your online Resume webpage.
* **NAME** : Enter your Full Name.
* **DESCRIPTION** : Enter your Description or Overview.

###  _03_social_media.json_

This section contains your Social Media links.

```json
{
  "MAX_SOCIAL_MEDIA_COLUMNS" : 5,
  "SOCIAL_MEDIA" : {}
}
```

To customize this section, navigate to `/assets/03_social_media.json` file and update the following values:
* **MAX_SOCIAL_MEDIA_COLUMNS** : Enter the maximum number of Values or Columns to display within a Row.
* **SOCIAL_MEDIA** : Enter your Social Media links in `"Platform" : "Link"` format.

###  _04_skills.json_

This section contains your Technical Skills.

```json
{
  "MAX_SKILLS_COLUMNS" : 5,
  "SKILLS" : []
}
```

To customize this section, navigate to `/assets/04_skills.json` file and update the following values:
* **MAX_SKILLS_COLUMNS** : Enter the maximum number of Values or Columns to display within a Row.
* **SKILLS** : Enter the list of your Skills.

###  _05_work_experience.json_

This section contains your Work Experience till date. Kindly list your experience in reverse chronological order.

```json
{
  "WORK_EXPERIENCE": [
    {
      "DESIGNATION" : "",
      "COMPANY" : "",
      "DURATION" : "",
      "DETAILS" : []
    }
  ]
}
```

To customize this section, navigate to `/assets/05_work_experience.json` file and update the following values:
* **WORK_EXPERIENCE** : Enter your work experience as list of object (mentioned below).
  * **DESIGNATION** : Enter your Designation or Role.
  * **COMPANY** : Enter the Name of the Company.
  * **DURATION** : Enter the Start Date and End Date in `Month, Year` format.
  * **DETAILS** : Enter the list of statements to showcase your impact.

###  _06_education.json_

This section contains your Education till date. Kindly list your experience in reverse chronological order. You may also disable this section, if you are a senior employee.

```json
{
  "EDUCATION": [
    {
      "COURSE" : "",
      "COLLEGE" : "",
      "DURATION" : "",
      "DETAILS" : []
    }
  ]
}
```

To customize this section, navigate to `/assets/06_education.json` file and update the following values:
* **EDUCATION** : Enter your Education details as list of object (mentioned below).
  * **COURSE** : Enter the name of your Course.
  * **COLLEGE** : Enter the Name of the College or University.
  * **DURATION** : Enter the Start Date and End Date in `Year` format.
  * **DETAILS** : Enter the list of statements to showcase your academic performance.

###  _07_projects.json_

This section contains your Projects. Kindly add links to the deployed creation or atleast the GitHub repository.

```json
{
  "PROJECTS": []
}
```

To customize this section, navigate to `/assets/07_projects.json` file and update the following values:
* **PROJECTS** : Enter the list of your Projects.

###  _08_publications.json_

This section contains your Publications. Kindly add links to the articles.

```json
{
  "PUBLICATIONS": []
}
```

To customize this section, navigate to `/assets/08_publications.json` file and update the following values:
* **PUBLICATIONS** : Enter the list of your Publications.

###  _09_public_speaking.json_

This section contains your Sessions. Kindly add links to the event photos, if possible.

```json
{
  "PUBLIC_SPEAKING": []
}
```

To customize this section, navigate to `/assets/09_public_speaking.json` file and update the following values:
* **PUBLIC_SPEAKING** : Enter the list of your Sessions.

###  _10_certificates.json_

This section contains your Certificates. Kindly add links to the Badges or Certificates.

```json
{
  "MAX_CERTIFICATES_COLUMNS" : 2,
  "CERTIFICATES" : {}
}
```

To customize this section, navigate to `/assets/10_certificates.json` file and update the following values:
* **MAX_CERTIFICATES_COLUMNS** : Enter the maximum number of Values or Columns to display within a Row.
* **CERTIFICATES** : Enter your Certificate links in `"Certificate" : "Link"` format.

###  _11_accomplishments.json_

This section contains your Accomplishments or Rewards. Kindly add links to the certificates, if possible.

```json
{
  "ACCOMPLISHMENTS": []
}
```

To customize this section, navigate to `/assets/11_accomplishments.json` file and update the following values:
* **ACCOMPLISHMENTS** : Enter the list of your Accomplishments or Rewards.

> Finally, we have updated all the necessary files and customized our Resume!! Take a short rest, and refresh the webpage.

> **3.. 2.. 1.. Your updated Resume is ready!!** 🎉

## Deploy on Streamlit Cloud

We have our Resume ready, but locally. Now we need to deploy it to the **Streamlit Cloud**, so that we can share it with various recruiters globally.

To deploy our code, we will follow these steps:
1. Upload the codebase to your GitHub repository, that you created in [Setup the Code locally](#setup-the-code-locally) step, using GitHub Desktop or GitHub web interface.
2. Navigate to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. **Sign Up** to create your account.
4. Link your GitHub account.
5. Navigate to the homepage and click on the **New App** button. ![New App](/documentation/new_app.jpg)
6. Update the following configuration.
   * Select your GitHub **Repository**. 
   * Keep the **Branch** as `main`. 
   * Update **Main file path** to `app.py`. 
   * Customize the **App URL**. ![Deploy Config](/documentation/deploy_config.jpg)
7. Click on the **Deploy!** button.
8. Kindly ensure that, your App is publicly accessible. ![Public Access](/documentation/public_access.jpg)

You can also refer to [How to Deploy Your App to Streamlit Community Cloud](https://www.youtube.com/watch?v=HKoOBiAaHGg) video on Youtube, for more clarification.

> **Taadaaaaa!! Your online Resume is ready for new exciting Opportunities!!** 🎊

## Examples

Here are few resume, that was created using this Resume Template:
* [**Sandip Palit**](https://sandippalit-resume.streamlit.app/)

If you would like us to Showcase your profile, kindly share your details in the [Discussion](https://github.com/SandipPalit/Resume-Template/discussions) tab.

## Reach out to Us

If you have any doubts, kindly let us know in the [Discussion](https://github.com/SandipPalit/Resume-Template/discussions) tab.

If you encounter any Bug or Issues, kindly raise them in the [Issues](https://github.com/SandipPalit/Resume-Template/issues/new?template=bug_report.md) tab.

If you would like to help us with Feature requests, kindly share them in the [Issues](https://github.com/SandipPalit/Resume-Template/issues/new?template=feature_request.md) tab.

Feel free to reach out to the creator, **Sandip Palit** on [Linkedin](https://www.linkedin.com/in/sandip-palit/).

---

> **_Please share your valuable feedback in the [Discussion](https://github.com/SandipPalit/Resume-Template/discussions) tab, and support this [Resume Template repository](https://github.com/SandipPalit/Resume-Template) by giving a 🌟_**.