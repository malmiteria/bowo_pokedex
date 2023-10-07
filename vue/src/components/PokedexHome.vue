<template>
    <div class="pokedex">
		<h1>Pokedex</h1>
		<ul class="pokemon_list">
			<li v-for="pokemon in pokemons" :key="pokemon.id">
				<h2>{{ pokemon.name }}</h2>
				<img :src=imageURL(pokemon)>
				<button @click="toggleTask(pokemon)">
					{{ pokemon.completed ? 'Undo' : 'Complete' }}
				</button>
			</li>
		</ul>
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
                    console.log(pokemon);
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
