export async function searchProducts(query: string) {
	const res = await fetch(`/api/v1/search?q=${encodeURIComponent(query)}`);

	if (!res.ok) {
		throw new Error('API Error');
	}

	return res.json();
}
