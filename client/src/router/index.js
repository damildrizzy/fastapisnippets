import {createRouter, createWebHistory} from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import SnippetCreate from "@/views/SnippetCreate";
import SnippetDetail from "@/views/SnippetDetail";
import store from "../store";

const routes = [
    {
        path: "/",
        alias: "/snippets",
        name: "Home",
        component: Home,
    },
    {
        path: "/login",
        name: "Login",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(/* webpackChunkName: "login" */ "../views/Login.vue"),
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
    },
    {
        path: "/create",
        name: "SnippetCreate",
        component: SnippetCreate,
        meta: {requiresAuth: true},
    },
    {
        path: "/snippets/:id",
        name: "snippet-detail",
        component: SnippetDetail,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

// eslint-disable-next-line no-unused-vars
router.beforeEach((to, from) => {
    // instead of having to check every route record with
    // to.matched.some(record => record.meta.requiresAuth)
    if (to.meta.requiresAuth && !store.state.auth.status.loggedIn) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        return {
            path: "/login",
            // save the location we were at to come back later
            query: {redirect: to.fullPath},
        };
    }
});

export default router;
