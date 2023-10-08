import { createWebHistory, createRouter } from "vue-router";
import PokedexHome from "@/components/PokedexHome.vue";
import OnePokemon from "@/components/OnePokemon.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: PokedexHome,
  },
  {
    path: "/pokemon/:id",
    name: "OnePokemon",
    component: OnePokemon,
	props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
