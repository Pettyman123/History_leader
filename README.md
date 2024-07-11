<h1>Historical Leaders Website</h1>
<body>This project is a Django-based web application that provides information about historical leaders from various countries. Users can view a list of important leaders, search for specific leaders, and view detailed profiles, including images, summaries, achievements, and links to their Wikipedia pages.
</body>

<h2>Features</h2>
<li>Home Page: Overview of the website with a search bar for quick access.</li>
<li>Country Page: List of countries with notable leaders.</li>
<li>Leader Profiles: Detailed information about each leader, including their lifetime, achievements, and a link to their Wikipedia page.</li>
<li>Traits: Leaders can have various traits such as "martyred", "dictator", "revolutionary", "populist", "autocrat", "reformist", and "businessman".</li>
<li>Responsive Design: Uses Bootstrap for a responsive and visually appealing design.</li>

<h2>Installation</h2>
<li>CLone repo
<ol>
  <li>git clone https://github.com/your-username/historical-leaders.git</li>
  <li>cd historical-leaders</li>

</ol>
</li>
<li>Create Virtual Env
<ol>
  <li>python -m venv venv</li>
  <li>source venv/bin/activate  # On Windows use `venv\Scripts\activate`</li>
</ol>
</li>
<li>Install dependencies
<ol>
  <li>pip install -r requirements.txt</li>
</ol>
</li>
<li>Run migrations
<ol>
  <li>python manage.py makemigrations</li>
  <li>python manage.py migrate</li>
</ol>
</li>
<li>Create Superuser
<ol>
  <li>python manage.py createsuperuser</li>
</ol>
</li>
<li>Run development server
<ol>
  <li>python manage.py runserver</li>
</ol>
</li>
<li>Acess the web application
<ol><li>CLICK ON THE http://127.0.0.1:8000/</li></ol>
</li>

<h2>Admin Panel</h2>
To add or modify data, log in to the admin panel:

<li>Go to http://127.0.0.1:8000/admin/.</li>
<li>Log in with the superuser credentials created earlier.</li>
<li>Add countries and leaders with their respective details.</li>


<h2>Contributing</h2>
<ol>
<li>Fork the repository.</li>
<li>Create your feature branch (git checkout -b feature/awesome-feature).</li>
<li>Commit your changes (git commit -m 'Add some awesome feature').</li>
<li>Push to the branch (git push origin feature/awesome-feature).</li>
<li>Open a pull request.</li>
</ol>

<h2>License</h2>
This project is licensed under the MIT License - see the LICENSE file for details.
<h3>CREATED BY:- GOURAV SHARMA</h3>
<h4>This documentation should provide a comprehensive guide for setting up, using, and contributing to the Historical Leaders website project.</h4>
