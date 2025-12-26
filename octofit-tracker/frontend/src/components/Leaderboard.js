
import React, { useState, useEffect } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

function Leaderboard() {
	const [leaderboard, setLeaderboard] = useState([]);
	useEffect(() => {
		console.log('Fetching leaderboard from:', API_URL);
		fetch(API_URL)
			.then(res => res.json())
			.then(data => {
				const results = data.results || data;
				setLeaderboard(results);
				console.log('Fetched leaderboard:', results);
			})
			.catch(err => console.error('Error fetching leaderboard:', err));
	}, []);
	return (
		<div className="card">
			<div className="card-body">
				<h2 className="card-title mb-4">Leaderboard</h2>
				<div className="table-responsive">
					<table className="table table-striped table-bordered">
						<thead className="table-primary">
							<tr>
								<th>#</th>
								<th>Team</th>
								<th>Points</th>
							</tr>
						</thead>
						<tbody>
							{leaderboard.map((l, i) => (
								<tr key={i}>
									<td>{i + 1}</td>
									<td>{l.team}</td>
									<td>{l.points}</td>
								</tr>
							))}
						</tbody>
					</table>
				</div>
			</div>
		</div>
	);
}

export default Leaderboard;
