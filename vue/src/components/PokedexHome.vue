<template>
    <div class="pokedex">
		<h1>Pokedex</h1>
		<form class="m-5" @submit.prevent="search">
			<p class="block text-gray-500 font-bold">You can filter pokemons by name or type (empty search doesn't filter).</p>
			<input class="bg-gray-200 appearance-none border-2 border-gray-200 rounded m-2" type="text" name="search_field"/>
			<input class="shadow bg-gray-500 hover:bg-purple-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="submit" value="search"/>
		</form>
		<form class="" @submit.prevent="sort">
			<p class="block text-gray-500 font-bold">You can sort pokemons by number, height or weight.</p>
			<select class="m-2 appearance-none bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" name="sort_field">
				<option value="pokedex_number">number</option>
				<option value="height_m">height</option>
				<option value="weight_kg">weight</option>
			</select>
			<input class="shadow bg-gray-500 hover:bg-purple-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="submit" value="sort"/>
		</form>
		<div class="grid grid-cols-5 gap-4 m-5">
			<div v-for="pokemon in pokemons" :key="pokemon.id">
				<div @click="pokemon_page(pokemon)" class="border-solid border-2 grid place-items-center">
					<h2>{{ pokemon.name }}</h2>
					<p>pokemon number: {{ pokemon.pokedex_number }}</p>
					<img :src=imageURL(pokemon)>
				</div>
			</div>
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
            async sort(formData) {
				const sortBy = formData.target.elements.sort_field.value;
				this.pokemons.sort((a, b) => {
					if (a[sortBy] < b[sortBy]) return -1
					if (a[sortBy] > b[sortBy]) return 1
					return 0;
				});
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
