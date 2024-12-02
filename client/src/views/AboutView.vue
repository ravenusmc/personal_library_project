<template>
  <div>

    <!-- Header area -->
    <div class="about_header">
      <h1 class="center title">My Story</h1>
    </div>
    <!-- End of Header Area -->

    <!-- Start of content area -->
    <div class="about_content_area">
      <div class="pic_div"></div>

      <div class="bio_div">
        <p>
          In the spring of 2015, I chose to take a leap in a new direction and
          immerse myself in learning full stack web development. I attended the
          coding bootcamp Tech Talent South as well as Gwinnett Technical
          College for a degree in web development. Since then, I have fully
          immersed myself in the Atlanta tech community attending meetups,
          conferences as well as hackathons to grow as a developer. I’ve won
          first place two years in a row at the SkillsUSA state level, in web
          design, and competed at the national level. I’ve worked with Manning
          Publications to help review many of their books/videos on the latest
          technology trends. I continue to work to stay up to date with the
          latest technologies by using such resources as Team Treehouse and
          Udemy. My casual interest in web development has now become a guiding
          passion and I am excited to bring that passion to my next pursuit.
        </p>

        <p>
          The experience I have earned in the Marine Corps and C.I.A. has
          awarded me confidence and ability to be successful in any field. I’ve
          proven an ability to work well under pressure when I had three months
          to prepare 40 Marines for a deployment to Camp Fallujah, Iraq. I’ve
          demonstrated communication skills was when I had to write a new convoy
          operations manual for the unit I served with in Afghanistan as well as
          giving 79 convoy briefs in Iraq. My ability to plan has been
          established when I planned 15 convoys across South Korea moving over
          1,000 pieces of decking, tents and aircraft equipment.
        </p>

        <p>
          Feel free to send me an invite; I’d love to connect with you.
        </p>
      </div>
    </div>
    <!-- End of content area -->

  </div>
</template>

<script>
</script>

<style lang="css" scoped>
.center {
  text-align: center;
}

/* CSS for header area */

.about_header {
  margin-top: 50px;
  margin-bottom: 50px;
}

.title {
  text-transform: uppercase;
}

/* CSS for content */
.about_content_area {
  display: flex;
  justify-content: space-around;
  margin: 0 5% 50px; /* Combine margin properties */
}

.pic_div {
  width: 300px;
  height: 400px; /* Set height to match width */
  border-radius: 10px;
  background: url("../assets/images/Cuddy.jpg") center/cover no-repeat; /* Combine background properties */
}

.bio_div {
  width: calc(100% - 320px); /* Calculate width based on remaining space */
  max-width: 600px; /* Limit maximum width */
}

/* Responsive only for mobile screens at this point */
@media only screen and (max-width: 768px) {

  .about_content_area {
    display: flex; 
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .bio_div {
    width: 100%;
  }

}
</style>



<!-- I'd love to help with your landing page! Here are some ideas and suggestions for creating an engaging and functional landing page for your personal library:

1. Hero Section
Visual Impact: Use a high-quality image or illustration of a cozy reading nook, shelves full of books, or an open book with glowing pages.
Headline:
"Welcome to My Personal Library"
"A World of Stories at Your Fingertips"
Subheading:
"Explore, Organize, and Rediscover Your Collection."
Call-to-Action (CTA):
"Browse Collection" or "Get Started"
2. About Section
Share your story:
Why you built the library.
What kind of books it contains (e.g., genres, rare finds, personal favorites).
Include a photo of your library or a visual that reflects its personality. -->