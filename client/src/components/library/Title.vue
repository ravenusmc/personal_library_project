<template>
    <div>
        <div class="title-div">
            <h1 class="title center">
                <span class="decorative">The</span>
                <span class="decorative highlight">Library</span>
            </h1>
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
/* Outer container */
.title-div {
    background: linear-gradient(to bottom, #f5f0e1, #eae4d0);
    border: 5px solid #5a4634;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    max-width: 800px;
    margin: 40px auto;
}

/* Main title styling */
.title {
    font-family: 'Merriweather', serif; /* A classic, bookish font */
    font-size: 4rem;
    color: #3e2c1c; /* Rich brown, bookish tone */
    text-shadow: 0 2px 2px rgba(0, 0, 0, 0.2);
    margin: 0;
}

/* Decorative words for emphasis */
.decorative {
    display: inline-block;
    font-style: italic;
    position: relative;
    padding-right: 10px;
}

/* Add a subtle underline to each word */
.decorative:after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -5px;
    width: 100%;
    height: 2px;
    background: linear-gradient(to right, #8b4513, #d2b48c);
}

/* Highlight "Library" with a gold touch */
.highlight {
    color: #b8860b; /* Golden brown */
    font-weight: bold;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Add a subtle bookish animation */
.decorative {
    animation: fade-in 2s ease-out;
}

/* Keyframe animations */
@keyframes fade-in {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
