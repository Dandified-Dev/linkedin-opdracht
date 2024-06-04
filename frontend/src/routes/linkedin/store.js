export const apiData = writable([]);
export const profiles = derived(apiData, ($apiData) => {
    if ($apiData.first_name) {
      return $apiData.first_name.map((first_name, i) => ({ first_name, last_name: $apiData.last_name[i], headline: $apiData.headline[i], location: $apiData.location[i], industry: $apiData.industry[i], summary: $apiData.summary[i], picture: $apiData.picture[i], profile_url: $apiData.profile_url[i] }));
    }
    return [];
  });