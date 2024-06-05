<script>
  import { onMount } from "svelte";
  import Card from "./Card.svelte";
  import Filter from "./Filter.svelte";

  let apiData = [];
  let filters = [];
  let filteredItem = "Alle";
  let filteredData = [];

  onMount(async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/profiles");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      apiData = await response.json();
      filters = ["Alle", ...new Set(apiData.flatMap(item => item.skills.map(skill => skill.skill_name)))];
    } catch (error) {
      console.error("Fetch error:", error);
    }
  });

  function selectFilter(event) {
    filteredItem = event.detail;
    if (filteredItem === "Alle") {
      filteredData = [];
    } else {
      filteredData = apiData.filter(item => item.skills.some(skill => skill.skill_name === filteredItem));
    }
  }
</script>

<!-- filter based on skills -->
<section class="dropdown">
  <Filter filteredItems={filters} on:selectFilter={selectFilter} />
</section>

<div class="flex flex-col items-center">
  <ul class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-4">
    {#if filteredData.length === 0}
      {#each apiData as item}
        <li class="">
          <Card data={item} />
        </li>
      {/each}
    {:else}
      {#each filteredData as item}
        <li class="">
          <Card data={item} />
        </li>
      {/each}
    {/if}
  </ul>
</div>

<style>		
  .dropdown {
    position: relative;
    display: inline-block;
  }
</style>
