<script>
  import { onMount } from "svelte";
  import Card from "./Card.svelte";
  import Button from './Button.svelte';
  import Link from './Links.svelte';

  let menuOpen = false;
  let inputValue = "";
  var apiData = [];
  var filters = [];
  let filteredItems = [];
  let filteredItem = "";
  let filteredData = [];

  onMount(async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/profiles");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      apiData = data;
      filters.push("Alle")
      for (let i = 0; i < apiData.length; i++) {
        for(let j = 0; j < apiData[i].skills.length; j++){
          filters.push(apiData[i].skills[j].skill_name);
        }
      }
      console.log("filters", filters);
      console.log("apiData", apiData);
      filteredItems = filters; // Initially populate filteredItems with all filters
    } catch (error) {
      console.error("Fetch error:", error);
    }
  });

  function selectFilter(event) {
    filteredItem = event.detail;
    menuOpen = false;
    filteredData = apiData.filter((item) => item.skills.some((skill) => skill.skill_name === filteredItem));
  }
</script>

<!-- filter based on skills -->
<section class="dropdown">
  <Button on:click={() => menuOpen = !menuOpen} {menuOpen} />
	
  <div id="myDropdown" class:show={menuOpen} class="dropdown-content">
		{#if filteredItems.length > 0}
			{#each filteredItems as item}
				<Link on:selectFilter={selectFilter} link={item} />
			{/each}
		{:else}
			<p>No filters found</p>
		{/if}		
  </div>	
</section>

<div class="flex flex-col items-center">
  <ul class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-4">
    {#if filteredItem === "Alle" || filteredItem === ""}
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
    {#each filteredData as item}
      <li class="">
        <Card data={item} />
      </li>
    {/each}
  </ul>
</div>

<style>		
  .dropdown {
    position: relative;
    display: inline-block;
  }
    
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f6f6f6;
    min-width: 230px;
    border: 1px solid #ddd;
    z-index: 1;
  }
  
  /* Show the dropdown menu */	
  .show {display:block;}	
</style>
