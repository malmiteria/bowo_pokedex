<template>
    <div class="pokedex">
		<h1>Pokedex</h1>
		<form @submit.prevent="search">
			<p>You can filter pokemons by name.</p>
			<input type="text" name="search_field"/>
			<input type="submit" value="search"/>
		</form>
		<div @click="pokemon_page(pokemon)" v-for="pokemon in pokemons" :key="pokemon.id">
			<h2>{{ pokemon.name }}</h2>
			<p>pokemon number: {{ pokemon.pokedex_number }}</p>
			<img class="pokeface" :src=imageURL(pokemon)>
		</div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                pokemons: ['']
            }
        },
        methods: {
            async getData() {
                try {
					console.log("getData");
                    // fetch tasks
                    const response = await this.$http.get('http://localhost:8000/pokedex/pokemon');
                    // set the data returned as tasks
                    this.pokemons = response.data; 
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
            async search(formData) {
				const filter = formData.target.elements.search_field.value;
                try {
                    // fetch tasks
                    const response = await this.$http.get('http://localhost:8000/pokedex/pokemon/?search=' + filter.toString());
                    // set the data returned as tasks
                    this.pokemons = response.data;
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
			pokemon_page(pokemon) {
				window.location.href = "/pokemon/" + pokemon.pokedex_number;
			},
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>

<style>
.pokeface {
  width: 150px;
  height: 150px;
}
</style>
