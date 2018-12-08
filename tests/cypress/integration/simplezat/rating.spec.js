context('Actions', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/ratings')
  })

  it('should be able to give positive rating with comment', () => {
    cy.contains('How do we do?')
    cy.get('[href="/ratings/positive/"] > img').should('have.attr', 'alt', 'Positive')
    cy.get('[href="/ratings/neutral/"] > img').should('have.attr', 'alt', 'Neutral')
    cy.get('[href="/ratings/negative/"] > img').should('have.attr', 'alt', 'Negative')

    cy.get('[href="/ratings/positive/"] > img').click()
    cy.wait(1000)

    cy.contains('Any comment?')
    cy.get('input[name="comment"]').type('You are doing great!')
    cy.get('button').click()
    cy.wait(1000)

    cy.contains('Thank you')
  })
})
