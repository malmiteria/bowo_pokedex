<template>
    <div class="pokedex">
		<h1>{{ pokemon.name }}</h1>
		<h3>{{ pokemon.japanese_name }}</h3>
		<p>pokemon number: {{ pokemon.pokedex_number }}</p>
		<p>pokemon type1: {{ pokemon.type1 }}</p>
		<p>pokemon type2: {{ pokemon.type2 }}</p>
		<p>pokemon classification: {{ pokemon.classification }}</p>
		<p>pokemon attack: {{ pokemon.attack }}</p>
		<p>pokemon defense: {{ pokemon.defense }}</p>
		<p>pokemon sp attack: {{ pokemon.sp_attack }}</p>
		<p>pokemon sp defense: {{ pokemon.sp_defense }}</p>
		<p>pokemon hp: {{ pokemon.hp }}</p>
		<p>pokemon speed: {{ pokemon.speed }}</p>
		<p>pokemon heigh (m): {{ pokemon.height_m }}</p>
		<p>pokemon weight (kg): {{ pokemon.weight_kg }}</p>
		<p>pokemon generation: {{ pokemon.generation }}</p>
		<p>pokemon is legendary: {{ pokemon.is_legendary }}</p>
		<img class="one_poke_please" :src=imageURL(pokemon)>
    </div>
</template>

<script>
    export default {
        props: ["id"],
        data() {
            return {
                pokemon: {}
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch tasks
                    const response = await this.$http.get('http://localhost:8000/pokedex/pokemon/' + this.id);
                    // set the data returned as tasks
                    this.pokemon = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
            imageURL(pokemon) {
                if (pokemon.id === undefined) {
					return;
                }
                var pokemon_3_digit_id = pokemon.id.toString();
				while (pokemon_3_digit_id.length < 3) pokemon_3_digit_id = "0" + pokemon_3_digit_id;
                return "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/" + pokemon_3_digit_id + ".png";
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>

<style>
.one_poke_please {
  width: 450px;
  height: 450px;
}
</style>
