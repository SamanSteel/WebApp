export interface Product {
	'کد کالا': string;
	'نام کالا': string;
	'محل کالا': string;
}

export interface CostCenter {
	'کد مرکز هزینه': string;
	'نام مرکز': string;
}

const BASE = 'http://192.168.20.19:9000/api/search';

async function request<T>(url: string): Promise<T> {
	const res = await fetch(url);

	if (!res.ok) {
		throw new Error(`HTTP ${res.status}`);
	}

	return res.json();
}

export async function searchProducts(query: string) {
	return request<{ items: Product[] }>(`${BASE}/product?q=${encodeURIComponent(query)}`);
}

export async function searchCostCenters(query: string) {
	return request<{ items: CostCenter[] }>(`${BASE}/cost-center?q=${encodeURIComponent(query)}`);
}
