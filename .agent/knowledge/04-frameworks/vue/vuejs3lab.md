---json
{
  "id": "vuejs3lab",
  "title": "Vuejs3Lab",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Vuejs3Lab.",
  "gatilhos": [
    "frameworks",
    "vue",
    "vuejs3lab"
  ],
  "perguntas_tipo": [
    "Como utilizar Vuejs3Lab?",
    "Quais as boas praticas de vue?"
  ],
  "nao_cobre": [],
  "target_agent": [
    "general-assistant"
  ],
  "source": {
    "origin": "AllMight Knowledge Base",
    "original_format": "markdown"
  },
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-vue",
  "prioridade": 2
}
---

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **

**Introduction **

Vue.js is an open-source **model–view–viewmodel** front end JavaScript **Library / framework** for building user 
interfaces and single-page applications. 




**LAB 1 : Getting Started with Vue 3 ( Vite ) **

1.​** Install Node.js (if not installed) : **Download from https ://nodejs.org 

Verify : 

**●​**** node -v **
**●​**** npm -v **

** **

**2.​ Create a new Vue 3 project : **

**○​**** npm create vite@latest vue-lab1 -- --template vue **

**○​**** cd vue-lab1 **

**○​**** npm install **

**○​**** npm run dev **

⇒** **Open http ://localhost :5173 to see your app. 

3.​ Folder structure : 

○​ main.js : app entry point 

○​ App.vue : root component 

○​ components/ : place your components here 

1 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**LAB 2 :**** Data Binding and Events **

**Data Binding** means connecting your **data (JavaScript)** to the **DOM (HTML)**, so that when the data changes, the 

UI updates automatically 



**Template Syntax** 

**<template> **

  <div> 

    <p>Hello, {{ name }}</p> 

    <input v-model="name" placeholder="Enter name" /> 

    <button @click="sayHello">Say Hello</button> 

  </div> 

**</template> **

**<script setup> **

import { ref } from 'vue'; 

const name = ref('Vue Student'); 

function sayHello() {  alert(`Hello, ${name.value}!`); } 

**</script>** 

2 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**Explanation **

●​** {{ name }}** : Text interpolation 

●​** v-model="name"** : Two-way binding 

●​** @click="sayHello"** : Handles button click 

**Practice Exercise **

Create a form with : 

●​ Full Name input 

●​ Email input 

●​ Submit button that logs the inputs 

**LAB 3 : ****Conditional**** Rendering **

Conditional rendering lets you control **what is displayed** in the DOM depending on the **value of variables or **
**expressions **
** **

**<template> **

  <div> 

    <button @click="toggle">Toggle Details</button> 

    <p v-if="showDetails">These are secret details!</p> 

  </div> 

**</template> **

**<script setup> **

import { ref } from 'vue'; 


const showDetails = ref(false); 

const toggle = () => showDetails.value = !showDetails.value; 

**</script> **

** **

3 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**LAB 4 : Loops with**** v-for**** **

**Code **
**Output **

<template> 

  <ul> 

    <li v-for="(user, index) in users"  :key="index"> 

      {{ index + 1 }}. {{ user }} 

    </li> 

  </ul> 

</template> 

<script setup> 

const users = ['Ahmed', 'Bassem', 'Ayoub']; 

</script> 

** **

●​ 1.Ahmed 

●​ 2. Bassem 

●​ 3.Ayoub 

**Practice : **Add a button to add new names to the list using v-model. 







4 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**LAB 5 : ****Components and Props **

In Vue.js, a component is a reusable block of code — it encapsulates HTML, CSS, and JavaScript into one file. 

You can : 

**●​** Create custom elements like **<UserCard /> **

●​ Reuse the same logic multiple times 

●​ Keep your code organized and maintainable** **

✅** Steps **

1.​ Create a file **UserCard.vue**** **: 

**<template> **

  <div> 

    <p>Name : {{ name }}</p> 

  </div> 

**</template> **

**<script setup> **

defineProps(['name']); 

**</script>** 

2.​ Use it in **App.vue** : 

<UserCard name="Benabderrezak" /> 

**Don't forget to import **: 

<script setup> import UserCard from './components/UserCard.vue';  </script> 


5 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**LAB 6 : Event Emitting **

Let child components notify the parent. 


** **

✅** Child Component**** : ****MyButton.vue **

<template> 

  <button @click="$emit('clicked')">Click me</button> 

</template> 

✅** Parent (App.vue) **

<MyButton @clicked="handleClick" /> 

function handleClick() { 

  alert("Child button clicked"); 

} 

** **

** **

** **

6 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**LAB 7 : ****Computed & Watchers **

**What is a Computed Property ? **

A **computed property** is a **cached** value that depends on reactive data. It only re-evaluates when its dependencies 

change 

<script setup> 

import { ref, computed } from 'vue'; 
const count = ref(5); 
const double = computed(() => count.value * 2); 
</script> 
<template> 

  <p>Count: {{ count }}</p> 
  <p>Double: {{ double }}</p> 
</template> 

⇒ The double value is **automatically recalculated** when count changes 

**Watcher ? **

A **watcher** allows you to run custom code **when a specific value changes** 

<script setup> 

import { ref, watch } from 'vue'; 
const search = ref(''); 
watch(search, (newVal, oldVal) => { 
  console.log(`Search changed from ${oldVal} to ${newVal}`); 
}); 
</script> 
<template> 

  <input v-model="search" placeholder="Type to search..." /> 
</template> 

⇒ Vue** watches ****search** and **triggers** the watch() function on change. 


7 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**LAB 8 : API Requests with Axios **

-​
Axios is a popular JavaScript library used to make HTTP requests (GET, POST, etc.) from the browser or 

Node.js. 

-​
Vue does not include Axios by default, but it works perfectly with it 

-​
**Install axios**** : **npm install axios 

<script setup> 

import axios from 'axios'; 

import { ref, onMounted } from 'vue'; 

const countries = ref([]); 


onMounted(async () => { 

  const res = await axios.get('https ://restcountries.com/v3.1/all'); 

  countries.value = res.data; 

}); 

</script> 

<template> 

  <ul> 

    <li v-for="c in countries"  :key="c.cca3">{{ c.name.common }}</li> 

  </ul> 

</template> 



8 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**LAB 9 : Routing with Vue Router **

Vue Router is the **official routing library for Vue.js**. It lets you: 

●​ Create multi-page navigation (SPA) 

●​ Assign URLs to components 

●​ Handle dynamic routes like **/users/:id** 

**Step 1 : Install Vue Router **

**●​**** npm install vue-router** 

**Step 2 : Create the Router Configuration **

Create a file : **src/router/****index.js**** **

import { createRouter, createWebHistory } from 'vue-router'; 

import Home from '../views/Home.vue'; 

import About from '../views/About.vue'; 


const routes = [ 

  { path: '/', component: Home }, 

  { path: '/about', component: About } 

]; 


const router = createRouter({ 

  history: createWebHistory(), 

  routes 

}); 

export default router; 

9 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**Step 3 : Use Router in Your App **

In main.js : 

import { createApp } from 'vue'; 

import App from './App.vue'; 

import router from './router'; 

createApp(App).use(router).mount('#app'); 

**Step 4 : Add Router View and Links **

In App.vue : 

<template> 

  <div> 

    <nav> 

      <router-link to="/">Home</router-link> | 

      <router-link to="/about">About</router-link> 

    </nav> 


    <router-view></router-view> 

  </div> 

</template> 

●​ <router-link> creates clickable navigation 

●​ <router-view> is where the page component is shown 

** **

10 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**Step 5 : Create the Page Components** 

**File **
**Content **

**src/views/Home.vue** 
<template> 

  <h2>Home Page</h2> 

</template> 

**src/views/About.vue**** **
<template> 

  <h2>About Us</h2> 

</template> 

**Dynamic Routes Example **

**Route definition** : 

{ path: '/users/:id', component: UserProfile } 

**Usage in component** : 

<script setup> 

import { useRoute } from 'vue-router'; 

const route = useRoute(); 

const userId = route.params.id; 

</script> 

**Practice Task **

●​ Add a third page : /contact 

●​ Create Contact.vue in views/ 

●​ Link it using <router-link to="/contact">Contact</router-link>​


11 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
**LAB 10 : Project — Vue Contact Book **

**Features : **

●​ Form to add contact (name + phone) 

●​ List of contacts 

●​ Sort alphabetically 

●​ Use components 

**Next Step : Advanced Vue.js Topics ( Vue 3 ) **

●​** Composition API (advanced use) **

○​ setup(), ref, reactive, computed, watch 

○​ provide / inject 

○​ Creating reusable composables (e.g., useCounter(), useForm()) 

●​** Teleport **

○​ Move components like modals outside the root DOM 

●​** Custom Directives **

○​ Create custom behavior like v-focus, tooltips, etc. 

●​** Render Functions & JSX **

○​ Render elements programmatically using h() 

●​** Reusable Composables **

○​ Encapsulate logic into functions for reuse across components 

●​** Pinia State Management (Vuex alternative) **

○​ defineStore() for global state 

○​ Replaces Vuex in Vue 3 

●​** Vue Router Advanced **

○​ Route guards (beforeEach, meta fields) 

○​ Lazy-loading routes 

○​ Dynamic nested routes 

●​** Performance Optimization **

○​ Lazy load components 

○​ Virtual scrolling 

○​ Keep-alive + memoization 

12 


--------------------------------------------------

**Vuejs 3 Lab                                                                                                                                    Dr Benabderrezak **

** **
●​** Authentication with JWT **

○​ Axios + backend login 

○​ Store tokens securely (cookies/localStorage) 

○​ Axios interceptors 

●​** Testing Vue Apps **

○​ Unit testing with **Vitest** / **Jest **

○​ E2E testing with **Cypress **

●​** TypeScript with Vue **

○​ Strong typing in components and props 

○​ defineProps<T>(), defineEmits<T>() 

●​** Internationalization (i18n) **

○​ Support for multiple languages 

○​ Dynamic translation using vue-i18n​






13 

