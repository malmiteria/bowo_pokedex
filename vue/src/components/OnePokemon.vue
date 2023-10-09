<template>
    <div class="grid grid-cols-2">
		<div class="border-2 border-gray-400 grid place-items-center m-5">
			<h1>{{ pokemon.name }}</h1>
			<h3>{{ pokemon.japanese_name }}</h3>
			<img class="one_poke_please" :src=imageURL(pokemon)>
		</div>
		<div class="grid grid-cols-2 m-5">
			<div class="border-2 border-black">number</div><div class="border-2 border-black">{{ pokemon.pokedex_number }}</div>
			<div class="border-2 border-black">type1</div><div class="border-2 border-black">{{ pokemon.type1 }}</div>
			<div class="border-2 border-black">type2</div><div class="border-2 border-black">{{ pokemon.type2 }}</div>
			<div class="border-2 border-black">classification</div><div class="border-2 border-black">{{ pokemon.classification }}</div>
			<div class="border-2 border-black">attack</div><div class="border-2 border-black">{{ pokemon.attack }}</div>
			<div class="border-2 border-black">defense</div><div class="border-2 border-black">{{ pokemon.defense }}</div>
			<div class="border-2 border-black">sp attack</div><div class="border-2 border-black">{{ pokemon.sp_attack }}</div>
			<div class="border-2 border-black">sp defense</div><div class="border-2 border-black">{{ pokemon.sp_defense }}</div>
			<div class="border-2 border-black">hp</div><div class="border-2 border-black">{{ pokemon.hp }}</div>
			<div class="border-2 border-black">speed</div><div class="border-2 border-black">{{ pokemon.speed }}</div>
			<div class="border-2 border-black">heigh (m)</div><div class="border-2 border-black">{{ pokemon.height_m }}</div>
			<div class="border-2 border-black">weight (kg)</div><div class="border-2 border-black">{{ pokemon.weight_kg }}</div>
			<div class="border-2 border-black">generation</div><div class="border-2 border-black">{{ pokemon.generation }}</div>
			<div class="border-2 border-black">is legendary</div><div class="border-2 border-black">{{ pokemon.is_legendary }}</div>
		</div>
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
