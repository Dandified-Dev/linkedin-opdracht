<script>
    import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

	export let link;
  function selectFilter() {
    dispatch("selectFilter", link);
    }
</script>

<button on:click={selectFilter} class="black px-[12px] py-[16px] block hover:bg-[#ddd] w-full justify-start text-left">{link}</button>
