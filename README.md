Exp 1: W rite a program to create a student portfolio w ebpage using HTML 5 elements.

[Steps to Run:

1.	Open VS Code.

2.	Create a new file: portfolio.html.

3.	Copy the code from Exp 1 into it.

4.	Save the file.

5.	Right-click → Open with Live Server (or double-click the file to open in a browser).

✅ You’ll see your portfolio web page.

]

Code:

<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Akshat's Portfolio</title>



  <!-- Bootstrap CSS -->

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">



  <style>

    body {

      background-color: rgb(220, 192, 218);

      font-family: Arial, sans-serif;

      scroll-behavior: smooth;

    }

    section {

      padding: 50px 20px;

      text-align: center;

    }

    h1 {

      color: blue;

      margin-bottom: 20px;

    }

    table {

      margin: auto;

      border-collapse: collapse;

      width: 80%;

    }

    th, td {

      border: 3px solid black;

      padding: 10px;

      font-size: 24px;

    }

    th {

      background-color: #f0f0f0;

    }

  </style>

</head>



<body>



  <!-- Navbar -->

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">

    <div class="container-fluid">

      <a class="navbar-brand" href="#">Akshat's Portfolio</a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">

        <span class="navbar-toggler-icon"></span>

      </button>



      <div class="collapse navbar-collapse" id="navbarNav">

        <ul class="navbar-nav ms-auto">

          <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>

          <li class="nav-item"><a class="nav-link" href="#basic">Basic Info</a></li>

          <li class="nav-item"><a class="nav-link" href="#academic">Academic Info</a></li>

        </ul>

      </div>

    </div>

  </nav>



  <!-- Home Section -->

  <section id="home">

    <br><br><br>

    <h1 style="font-size: 70px;">Welcome To Akshat's Portfolio!!</h1>

    <img src="photo.jpg" alt="Profile Pic" width="400px">

    <p style="font-size: 30px;">Department of Information Technology | APSIT</p>

  </section>



  <!-- Basic Info Section -->

  <section id="basic">

    <h1 style="font-size: 60px;">Basic Information</h1>

    <p style="font-size: 25px;"><b>Name:</b> Akshat Madheshiya</p>

    <p style="font-size: 25px;"><b>Email:</b> akshat@gmail.com</p>

    <p style="font-size: 25px;"><b>Contact:</b> 8329973490</p>

    <p style="font-size: 25px;"><b>About Me:</b> I love to read books and am always curious to learn new things.</p>

    <p style="font-size: 25px;"><b>Address:</b> Thane</p>



    <p style="font-size: 25px;"><b>Skills:</b></p>

    <ul style="list-style-position: inside; font-size: 25px;">

      <li>C</li>

      <li>C++</li>

      <li>Java</li>

      <li>Python</li>

    </ul>



    <p style="font-size: 25px;"><b>Projects Made By Me:</b></p>

    <ol style="list-style-position: inside; font-size: 25px;">

      <li>Recipe App</li>

      <li>StudySync: Study Planner</li>

    </ol>

  </section>



  <!-- Academic Info Section -->

  <section id="academic">

    <h1 style="font-size: 60px;">My Academic Qualifications</h1>

    <table>

      <tr>

        <th>Qualification</th>

        <th>Name of School/College</th>

        <th>Board/University</th>

        <th>Percentage/CGPA</th>

      </tr>

      <tr>

        <td>SSC</td>

        <td>Shreerang Vidyalaya</td>

        <td>State Board</td>

        <td>92.80</td>

      </tr>

      <tr>

        <td>HSC</td>

        <td>N.K.T.T</td>

        <td>State Board</td>

        <td>84.50</td>

      </tr>

      <tr>

        <td>Semester 1</td>

        <td>APSIT</td>

        <td>Mumbai University</td>

        <td>9.89</td>

      </tr>

      <tr>

        <td>Semester 2</td>

        <td>APSIT</td>

        <td>Mumbai University</td>

        <td>9.60</td>

      </tr>

      <tr>

        <td>Semester 3</td>

        <td>APSIT</td>

        <td>Mumbai University</td>

        <td>10.00</td>

      </tr>

    </table>

  </section>



  <!-- Bootstrap JS -->

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>

Exp2: W rite a prog ram to create a p lacem en ts registration form using HT M L 5 Elements.

[Steps:

1.	Create a new file: placement.html.

2.	Paste the experiment code.

3.	Save and open it in a browser.

4.	Try submitting the form — JS validation will run automatically.

✅ Displays alerts for invalid entries or success messages.

]

Code:

<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Placement Registration Form</title>



  <style>

    body {

      background-color: lightyellow;

      font-family: Arial, sans-serif;

      margin: 20px;

    }

    fieldset {

      margin-bottom: 15px;

      padding: 15px;

      border-radius: 10px;

    }

    legend {

      font-weight: bold;

    }

    label {

      display: inline-block;

      width: 150px;

      margin-top: 8px;

    }

    input, select, textarea {

      margin-top: 5px;

    }

    input[type="submit"], input[type="reset"] {

      margin-top: 10px;

      padding: 6px 12px;

      font-weight: bold;

      cursor: pointer;

    }

  </style>

</head>



<body>

  <h1>Placement Registration Form</h1>



  <form onsubmit="return validateForm()">

    <fieldset style="background-color: #f7d9aa;">

      <legend>Personal Details</legend>



      <label for="name">Name:</label>

      <input type="text" id="name" placeholder="Enter your name"><br>



      <label>Gender:</label>

      <input type="radio" name="gender" value="Male"> Male

      <input type="radio" name="gender" value="Female"> Female<br>



      <label for="phone">Phone:</label>

      <input type="tel" id="phone" placeholder="10-digit number"><br>



      <label for="branch">Branch:</label>

      <select id="branch">

        <option value="">Select</option>

        <option>IT</option>

        <option>COMPS</option>

        <option>DS</option>

        <option>AIML</option>

      </select><br>



      <label for="email">Email:</label>

      <input type="email" id="email"><br>



      <label for="pass">Password:</label>

      <input type="password" id="pass"><br>



      <label for="rpass">Retype Password:</label>

      <input type="password" id="rpass"><br>

    </fieldset>



    <fieldset style="background-color: #b2f0f0;">

      <legend>Academic Details</legend>



      <label for="percent">Percentage:</label>

      <input type="text" id="percent" placeholder="e.g. 75"><br>



      <label>Certifications:</label><br>

      <input type="checkbox"> Python

      <input type="checkbox"> Networking

      <input type="checkbox"> C Essentials

      <input type="checkbox"> Linux Essentials<br><br>



      <label for="intern">Internship Completed?</label>

      <select id="intern">

        <option value="">Select</option>

        <option>Yes</option>

        <option>No</option>

      </select><br>

    </fieldset>



    <fieldset style="background-color: #d3d3d3;">

      <legend>File Upload</legend>



      <label for="resume">Upload Resume:</label>

      <input type="file" id="resume"><br>



      <label for="marksheet">Upload Marksheet:</label>

      <input type="file" id="marksheet"><br>

    </fieldset>



    <input type="submit" value="Submit">

    <input type="reset" value="Reset">

  </form>



  <script>

    function validateForm() {

      let name = document.getElementById("name").value.trim();

      let phone = document.getElementById("phone").value.trim();

      let email = document.getElementById("email").value.trim();

      let pass = document.getElementById("pass").value;

      let rpass = document.getElementById("rpass").value;

      let percent = document.getElementById("percent").value.trim();



      if (name === "") {

        alert("Please enter your name.");

        return false;

      }



      if (!/^[0-9]{10}$/.test(phone)) {

        alert("Please enter a valid 10-digit phone number.");

        return false;

      }



      if (!email.includes("@") || !email.includes(".")) {

        alert("Please enter a valid email address.");

        return false;

      }



      if (pass.length < 6) {

        alert("Password must be at least 6 characters long.");

        return false;

      }



      if (pass !== rpass) {

        alert("Passwords do not match!");

        return false;

      }



      if (isNaN(percent) || percent < 0 || percent > 100) {

        alert("Enter a valid percentage between 0 and 100.");

        return false;

      }



      alert("Form submitted successfully!");

      return true;

    }

  </script>

</body>

</html>

Exp3: Home Page of Commercial Website with CSS

[Steps:

1.	Create a folder website.

2.	Inside it:

o	Create web.html

o	Create shopping.css

3.	Paste HTML and CSS codes in respective files.

4.	Make sure the CSS file link in HTML is:

<link rel="stylesheet" href="shopping.css">

open web.html in a browser.

✅ You’ll see a styled e-commerce webpage.]

Code: web.html

<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Online Shopping</title>

  <link rel="stylesheet" href="shopping.css">

</head>



<body>

  <header>

    <h2>Online Shopping</h2>

    <input type="text" id="search" placeholder="Search Products...">

    <nav>

      <a href="#home">Home</a>

      <a href="#electronics">Electronics</a>

      <a href="#fashion">Fashion</a>

      <a href="#kitchen">Home & Kitchen</a>

      <a href="#books">Books</a>

      <a href="#more">More</a>

    </nav>

  </header>



  <main id="home">

    <h3>Featured Products</h3>

    <div class="containerProduct">



      <div class="product-card" id="electronics">

        <img src="https://cdn.mos.cms.futurecdn.net/eX6Rte42SVcQ6hYNiRAXx5.jpg" alt="Phone">

        <p>Smartphone</p>

        <p>Price: ₹20,999</p>

      </div>



      <div class="product-card" id="fashion">

        <img src="https://staranddaisy.in/wp-content/uploads/2022/04/197674hfg.jpg" alt="Dress">

        <p>Stylish Dress</p>

        <p>Price: ₹1,299</p>

      </div>



      <div class="product-card" id="books">

        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMyvDttHou2Jhx4oauMpOZWeEBMUMsKMvi_A&s" alt="Books">

        <p>Best Seller Books</p>

        <p>Price: ₹499</p>

      </div>



      <div class="product-card" id="more">

        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4pLKqeSVGSAbyrfGIKWXy6vVEjAy2o4ZwWg&s" alt="Toys">

        <p>Toy Set</p>

        <p>Price: ₹799</p>

      </div>



    </div>



    <section id="kitchen">

      <h3>Home & Kitchen Products</h3>

      <p>Find top-quality kitchen and home essentials here!</p>

    </section>

  </main>



  <footer>

    <p>&copy; 2025 Online Shopee. All Rights Reserved.</p>

  </footer>

</body>

</html>

shopping.css:

html {

  scroll-behavior: smooth;

}



/* Element Selector */

body {

  background-color: antiquewhite;

  margin: 0;

  font-family: Arial, sans-serif;

}



/* ID Selector */

#search {

  border-radius: 5px;

  padding: 6px;

  margin: 5px;

  border: none;

}



/* Element + Descendant Selector */

header {

  background-color: black;

  color: white;

  padding: 10px;

  text-align: center;

}



/* Element Selector for nav */

nav {

  background-color: grey;

  padding: 8px;

}



/* Class Selector */

.product-card {

  background-color: white;

  width: 180px;

  border-radius: 5px;

  text-align: center;

  padding-bottom: 10px;

  box-shadow: 0 2px 5px rgba(0,0,0,0.2);

  transition: transform 0.2s;

}



/* Pseudo-class Selector */

.product-card:hover {

  transform: scale(1.05);

}



/* Universal Selector */

* {

  box-sizing: border-box;

}



/* Group Selector */

nav a, footer p {

  color: white;

  text-decoration: none;

}



/* Pseudo-class for hover */

nav a:hover {

  color: yellow;

  text-decoration: underline;

}



/* Flexbox for container */

.containerProduct {

  display: flex;

  justify-content: center;

  flex-wrap: wrap;

  gap: 20px;

  margin-top: 20px;

}



/* Image styling */

.product-card img {

  width: 100%;

  height: 150px;

  border-top-left-radius: 5px;

  border-top-right-radius: 5px;

}



/* Footer styling */

footer {

  background-color: black;

  color: white;

  text-align: center;

  padding: 10px;

  margin-top: 20px;

}

Exp4: Enhance Styling using Bootstrap

[Steps:

1.	Create a file: bootstrap.html.

2.	Paste the full code.

3.	Make sure this line is present in <head>:

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

4.	Open the file in a browser.

✅ You’ll see a nicely styled portfolio using Bootstrap.]

Code:

<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8" />

  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>Akshat's Portfolio</title>



  <!-- Bootstrap CSS -->

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">



  <style>

    /* 🌈 General Styling */

    body {

      font-family: "Poppins", "Segoe UI", Tahoma, sans-serif;

      background: linear-gradient(135deg, #f0f9ff, #cbebff);

      color: #222;

      margin: 0;

      padding: 0;

    }



    /* 🧭 Header Section */

    header {

      background: linear-gradient(135deg, #0077b6, #00b4d8);

      color: white;

      text-align: center;

      padding: 70px 20px;

      box-shadow: 0 2px 10px rgba(0,0,0,0.2);

    }



    header h1 {

      font-weight: 700;

      font-size: 3rem;

      margin-bottom: 15px;

    }



    header p {

      font-size: 1.3rem;

      font-weight: 400;

      margin: 0;

      letter-spacing: 0.5px;

    }



    /* 📦 Section Styling */

    section {

      background: white;

      max-width: 900px;

      margin: 50px auto;

      padding: 40px 30px;

      border-radius: 12px;

      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);

    }



    h2 {

      border-left: 6px solid #0077b6;

      padding-left: 15px;

      font-weight: 600;

      color: #0077b6;

      margin-bottom: 25px;

    }



    /* 🎯 Skill Badges */

    .skill-badge {

      background-color: #00b4d8;

      color: white;

      padding: 10px 18px;

      border-radius: 25px;

      display: inline-block;

      margin: 5px;

      font-weight: 600;

      transition: 0.3s ease;

    }



    .skill-badge:hover {

      background-color: #0077b6;

      transform: scale(1.1);

      box-shadow: 0 2px 8px rgba(0, 119, 182, 0.4);

    }



    /* 🧾 Certificates List */

    ul {

      list-style-type: "⭐ ";

      font-size: 1.1rem;

      line-height: 1.8rem;

      padding-left: 25px;

    }



    /* 🦶 Footer */

    footer {

      text-align: center;

      padding: 20px 0;

      background-color: #e8f6ff;

      color: #555;

      font-size: 0.95rem;

      margin-top: 60px;

    }



    @media (min-width: 768px) {

      header h1 {

        font-size: 4rem;

      }



      header p {

        font-size: 1.5rem;

      }

    }

  </style>

</head>



<body>

  <!-- 🧭 Header -->

  <header>

    <h1>Hello, I'm Akshat</h1>

    <p>Information Technology Student</p>

  </header>



  <!-- 🧑 About Section -->

  <section id="about">

    <h2>About Me</h2>

    <p>

      I am passionate about technology, design, and coding. I love learning new programming languages and exploring innovative ways to solve problems using technology.

    </p>

  </section>



  <!-- 🎓 Education Section -->

  <section id="education">

    <h2>Education</h2>

    <p><strong>Third Year Information Technology Student</strong><br>Mumbai University</p>

    <p><strong>High School:</strong> NES</p>

  </section>



  <!-- 💡 Skills Section -->

  <section id="skills">

    <h2>Technical Skills</h2>

    <div>

      <span class="skill-badge">HTML</span>

      <span class="skill-badge">CSS</span>

      <span class="skill-badge">JavaScript</span>

      <span class="skill-badge">Bootstrap</span>

      <span class="skill-badge">Python</span>

      <span class="skill-badge">SQL</span>

    </div>

  </section>



  <!-- 🏅 Certificates Section -->

  <section id="certificates">

    <h2>Certificates</h2>

    <ul>

      <li>Oracle Certified Associate</li>

      <li>NPTEL Certification in Programming</li>

      <li>Coursera: Introduction to Web Development</li>

      <li>Microsoft Technology Associate</li>

      <li>Google IT Support Professional Certificate</li>

    </ul>

  </section>



  <!-- 🦶 Footer -->

  <footer>

    &copy; 2025 Akshat | Designed with ❤️ using HTML, CSS & Bootstrap

  </footer>



  <!-- Bootstrap JS -->

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>

Exp5: W rite a p ro g ram to imp le ment E S 6 functions

[Steps:

1.	Create a file: fibonacci.html.

2.	Paste the JavaScript code.

3.	Save and open in a browser.

4.	A prompt will appear asking how many Fibonacci numbers to print.

✅ Output will appear on screen.

]

Code:

<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>JavaScript Fibonacci</title>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

</head>



<body class="bg-light text-center p-5">



  <div class="container">

    <h2 class="mb-4 text-primary">Fibonacci Series Generator</h2>

    <button class="btn btn-success mb-3" onclick="generateFibonacci()">Generate Series</button>

    <div id="output" class="alert alert-info mt-3"></div>

  </div>



  <script>

    function generateFibonacci() {

      let num = parseInt(prompt("Enter how many numbers you want to print:"));

      if (isNaN(num) || num <= 0) {

        document.getElementById("output").innerHTML = "Please enter a valid positive number!";

        return;

      }



      let var1 = 0, var2 = 1;

      let result = "The Fibonacci Series is: " + var1 + " " + var2 + " ";



      for (let counter = 2; counter < num; counter++) {

        let sum = var1 + var2;

        result += sum + " ";

        var1 = var2;

        var2 = sum;

      }



      document.getElementById("output").innerHTML = result;

    }



    // Automatically run once when page loads

    generateFibonacci();

  </script>



</body>

</html>

Exp6: W rite a p rog ram to ap p ly valid ations to Registration F orm .

[Steps:

1.	Create validation.html.

2.	Paste all HTML and JS code.

3.	Open it in a browser.

4.Try entering invalid data : ✅ Alerts will guide you for incorrect input.]

Code:

<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Registration Form</title>

  <style>

    body {

      background-color: aquamarine;

      font-family: Georgia, 'Times New Roman', Times, serif;

    }

    .ff {

      background-color: aliceblue;

      font-size: 18px;

      padding: 20px;

      width: 300px;

      margin: 30px auto;

      border-radius: 8px;

    }

    h2 {

      text-align: center;

    }

  </style>

</head>



<body>

  <h2>Registration Form</h2>



  <form name="f1" class="ff" onsubmit="return val()">

    <fieldset>

      <legend>User Personal Information</legend>



      <label>Enter your name:</label><br>

      <input type="text" name="sname" required><br><br>



      <
