<script>
  import { createEventDispatcher } from "svelte";
  import Button from "./Button.svelte";
  import Link from "./Links.svelte";
  let menuOpen = false;
  const dispatch = createEventDispatcher();

  export let filteredItems = [];
  let filteredItem = "";
  function selectFilter(event) {
    filteredItem = event.detail;
    menuOpen = false;
    dispatch("selectFilter", filteredItem);
  }
</script>

<section class="dropdown">
  <Button on:click={() => (menuOpen = !menuOpen)} {menuOpen} />

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
      /* Set overflow-y to auto to enable scrolling */
      overflow-y: auto;
      /* Set max-height to limit the height of the dropdown */
      max-height: 200px; /* Adjust this value as needed */
    }
  
    /* Show the dropdown menu */
    .show {
      display: block;
    }
  </style>
