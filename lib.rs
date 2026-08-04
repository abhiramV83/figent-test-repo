// DELIBERATE QUALITY/PERFORMANCE ISSUE: deep loops nesting (O(N^3))
pub fn process_matrix(matrix: &Vec<Vec<Vec<i32>>>) -> i32 {
    let mut total = 0;
    for i in 0..matrix.len() {
        for j in 0..matrix[i].len() {
            for k in 0..matrix[i][j].len() {
                if matrix[i][j][k] > 0 {
                    total += matrix[i][j][k];
                }
            }
        }
    }
    total
}
